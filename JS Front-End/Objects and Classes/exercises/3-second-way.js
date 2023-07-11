function storeProvision(array1, array2) {
	const mergedArrays = [...array1, ...array2];
	const finalProducts = mergedArrays.reduce((products, item, index) => {
		if (index % 2 === 0) {
			if (products.hasOwnProperty(item)) {
				products[item] += Number(mergedArrays[index + 1]);
			} else {
				products[item] = Number(mergedArrays[index + 1]);
			}
		}
		return products;
	}, {});

	Object.entries(finalProducts).forEach(([product, quantity]) =>
		console.log(`${product} -> ${quantity}`)
	);
}

storeProvision(
	["Chips", "5", "CocaCola", "9", "Bananas", "14", "Pasta", "4", "Beer", "2"],
	["Flour", "44", "Oil", "12", "Pasta", "7", "Tomatoes", "70", "Bananas", "30"]
);
