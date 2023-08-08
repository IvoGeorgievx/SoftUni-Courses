function solve(input) {
	const horses = input.shift().split("|");

	while (input[0] !== "Finish") {
		const [command, horse, horse2] = input.shift().split(" ");

		if (command === "Retake") {
			if (horses.indexOf(horse) < horses.indexOf(horse2)) {
				const horseIndex = horses.indexOf(horse);
				const horse2Index = horses.indexOf(horse2);
				horses[horseIndex] = horse2;
				horses[horse2Index] = horse;
				console.log(`${horse} retakes ${horse2}.`);
			}
		} else if (command === "Trouble") {
			const horseIndex = horses.indexOf(horse);
			if (horseIndex > 0) {
				const newHorseIndex = horseIndex - 1;
				const horseToMove = horses.splice(horseIndex, 1)[0];
				horses.splice(newHorseIndex, 0, horseToMove);
				console.log(`Trouble for ${horse} - drops one position.`);
			}
		} else if (command === "Rage") {
			const horseIndex = horses.indexOf(horse);
			if (horseIndex <= horses.length - 2) {
				horses.splice(horseIndex, 1);
				horses.splice(horseIndex + 2, 0, horse);
				console.log(`${horse} rages 2 positions ahead.`);
			} else {
				horses.splice(horseIndex, 1);
				horses.push(horse);
				console.log(`${horse} rages 2 positions ahead.`);
			}
		} else if (command === "Miracle") {
			const miracleHorse = horses.shift();
			horses.push(miracleHorse);
			console.log(`What a miracle - ${miracleHorse} becomes first.`);
		}
	}
	console.log(horses.join("->"));
	console.log(`The winner is: ${horses[horses.length - 1]}`);
}
solve([
	"Onyx|Domino|Sugar|Fiona",
	"Trouble Onyx",
	"Retake Onyx Sugar",
	"Rage Domino",
	"Miracle",
	"Finish",
]);
