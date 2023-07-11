function inventory(array) {
	const result = array
		.reduce((acc, curr) => {
			let [name, level, items] = curr.split(" / ");
			level = Number(level);
			items = items.split(", ");
			acc.push({ name, level, items });
			return acc;
		}, [])
		.forEach((el) => console.log(JSON.stringify(el)));
	// console.log(array)
	return result;
}

inventory([
	"Isacc / 25 / Apple, GravityGun",
	"Derek / 12 / BarrelVest, DestructionSword",
	"Hes / 1 / Desolator, Sentinel, Antara",
]);
