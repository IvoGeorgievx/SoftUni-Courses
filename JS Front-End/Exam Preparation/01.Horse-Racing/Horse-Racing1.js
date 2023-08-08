function solve(input) {
	const horses = input.shift().split("|");

	while (input[0] !== "Finish") {
		const [command, horse, horse2] = input.shift().split(" ");

		if (command === "Retake") {
			if (horses.indexOf(horse) < horses.indexOf(horse2)) {
				const indexHorse = horses.indexOf(horse);
				const indexHorse2 = horses.indexOf(horse2);
				horses[indexHorse] = horse2;
				horses[indexHorse2] = horse;
				console.log(`${horse} retakes ${horse2}.`);
			}
		} else if (command === "Trouble") {
			const indexHorse = horses.indexOf(horse);
			if (indexHorse > 0) {
				horses.splice(indexHorse, 1);
				horses.splice(indexHorse - 1, 0, horse);
				console.log(`Trouble for ${horse} - drops one position.`);
			}
		} else if (command === "Rage") {
			const indexHorse = horses.indexOf(horse);
			if (indexHorse < horses.length - 2) {
				horses.splice(indexHorse, 1);
				horses.push(horse);
				console.log(`${horse} rages 2 positions ahead.`);
			} else {
				horses.splice(indexHorse, 1);
				horses.splice(indexHorse + 2, 0, horse);
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
	"Fancy|Lilly",
	"Retake Lilly Fancy",
	"Trouble Lilly",
	"Trouble Lilly",
	"Finish",
	"Rage Lilly",
]);
