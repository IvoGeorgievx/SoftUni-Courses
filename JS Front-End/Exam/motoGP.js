function solve(input) {
	const numberOfRacers = Number(input.shift());
	const racers = input.slice(0, numberOfRacers).reduce((acc, line) => {
		const [name, fuelCapacity, position] = line.split("|");
		acc[name] = {
			fuelCapacity: Number(fuelCapacity),
			position: Number(position),
		};
		return acc;
	}, {});
	const actions = input.slice(numberOfRacers);

	while (actions[0] !== "Finish") {
		const current = actions.shift();

		const command = current.split(" - ")[0];
		if (command === "StopForFuel") {
			const rider = current.split(" - ")[1];
			const minFuel = Number(current.split(" - ")[2]);
			const changedPos = Number(current.split(" - ")[3]);
			if (racers[rider].fuelCapacity < minFuel) {
				console.log(
					`${rider} stopped to refuel but lost his position, now he is ${changedPos}.`
				);
				racers[rider].position = changedPos;
			} else {
				console.log(`${rider} does not need to stop for fuel!`);
			}
		} else if (command === "Overtaking") {
			const rider1 = current.split(" - ")[1];
			const rider2 = current.split(" - ")[2];
			if (racers[rider1].position < racers[rider2].position) {
				const rider1Pos = Number(racers[rider1].position);
				const rider2Pos = Number(racers[rider2].position);
				racers[rider1].position = rider2Pos;
				racers[rider2].position = rider1Pos;
				console.log(`${rider1} overtook ${rider2}!`);
			}
		} else if (command === "EngineFail") {
			const rider = current.split(" - ")[1];
			const lapsLeft = Number(current.split(" - ")[2]);
			console.log(
				`${rider} is out of the race because of a technical issue, ${lapsLeft} laps before the finish.`
			);
			delete racers[rider];
		}
	}

	// const sorted = Object.entries(racers).sort(
	// 	(a, b) => a[1].position - b[1].position
	// );
	// sorted.forEach((racer) => {
	// 	console.log(`${racer[0]}`);
	// 	console.log(`  Final position: ${racer[1].position}`);
	// });
	for(let racer in racers){
		console.log(`${racer}`);
		console.log(`  Final position: ${racers[racer].position}`);
	}
}

solve([
	"3",
	"Valentino Rossi|100|1",
	"Marc Marquez|90|2",
	"Jorge Lorenzo|80|3",
	"StopForFuel - Valentino Rossi - 50 - 1",
	"Overtaking - Marc Marquez - Jorge Lorenzo",
	"EngineFail - Marc Marquez - 10",
	"Finish",
]);

// solve([
// 	"4",
// 	"Valentino Rossi|100|1",
// 	"Marc Marquez|90|3",
// 	"Jorge Lorenzo|80|4",
// 	"Johann Zarco|80|2",
// 	"StopForFuel - Johann Zarco - 90 - 5",
// 	"Overtaking - Marc Marquez - Jorge Lorenzo",
// 	"EngineFail - Marc Marquez - 10",
// 	"Finish",
// ]);
