function cookingByNums(num, ...commands) {
	let currentNum = Number(num);

	for (let i = 0; i < commands.length; i++) {
		let command = commands[i];
		if (command === "chop") {
			currentNum /= 2;
		} else if (command === "dice") {
			currentNum = Math.sqrt(currentNum);
		} else if (command === "spice") {
			currentNum += 1;
		} else if (command === "bake") {
			currentNum *= 3;
		} else {
			currentNum *= 0.8;
		}
		console.log(currentNum);
	}
}

cookingByNums("9", "dice", "spice", "chop", "bake", "fillet");
