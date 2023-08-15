function solve(input) {
	const flights = input.shift().reduce((acc, curr) => {
		const flightInfo = curr.split(" ");
		const flight = flightInfo.shift();
		const destination = flightInfo.join(" ");
		acc[flight] = { destination, status: "Ready to fly" };
		return acc;
	}, {});

	input.shift().reduce((acc, curr) => {
		const [flight, status] = curr.split(" ");
		if (flights.hasOwnProperty(flight)) {
			flights[flight].status = status;
		}
		return acc;
	}, {});

	const statusToCheck = input.shift()[0];

	Object.values(flights)
		.filter(({ status }) => status === statusToCheck)
		.forEach((flight) => {
			console.log(
				`{ Destination: '${flight.destination}', Status: '${flight.status}' }`
			);
		});
}

// solve([
// 	[
// 		"WN269 Delaware",
// 		"FL2269 Oregon",
// 		"WN498 Las Vegas",
// 		"WN3145 Ohio",
// 		"WN612 Alabama",
// 		"WN4010 New York",
// 		"WN1173 California",
// 		"DL2120 Texas",
// 		"KL5744 Illinois",
// 		"WN678 Pennsylvania",
// 	],
// 	[
// 		"DL2120 Cancelled",
// 		"WN612 Cancelled",
// 		"WN1173 Cancelled",
// 		"SK430 Cancelled",
// 	],
// 	["Cancelled"],
// ]);

solve([
	[
		"WN269 Delaware",
		"FL2269 Oregon",
		"WN498 Las Vegas",
		"WN3145 Ohio",
		"WN612 Alabama",
		"WN4010 New York",
		"WN1173 California",
		"DL2120 Texas",
		"KL5744 Illinois",
		"WN678 Pennsylvania",
	],
	[
		"DL2120 Cancelled",
		"WN612 Cancelled",
		"WN1173 Cancelled",
		"SK330 Cancelled",
	],
	["Ready to fly"],
]);
