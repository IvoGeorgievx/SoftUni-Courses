function storeProvision(array1, array2) {
    const finalProducts = {}
    for (let i = 0; i < array1.length; i += 2) {
        finalProducts[array1[i]] = Number(array1[i + 1])
    }
    for (let i = 0; i < array2.length; i += 2) {
        if (finalProducts.hasOwnProperty(array2[i])) {
            finalProducts[array2[i]] += Number(array2[i + 1])
        } else {
            finalProducts[array2[i]] = Number(array2[i + 1])
        }
    }

    Object.entries(finalProducts).forEach(x => console.log(`${x[0]} -> ${x[1]}`))
}

storeProvision(
	["Chips", "5", "CocaCola", "9", "Bananas", "14", "Pasta", "4", "Beer", "2"],
	["Flour", "44", "Oil", "12", "Pasta", "7", "Tomatoes", "70", "Bananas", "30"]
);
