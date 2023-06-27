function roadRadar(currentSpeed, area) {
	const speeds = {
		motorway: 130,
		interstate: 90,
		city: 50,
		residential: 20,
	};

	let difference = currentSpeed - speeds[area];
	let status = "";

	if (difference <= 0) {
		console.log(`Driving ${currentSpeed} km/h in a ${speeds[area]} zone`);
	} else if (difference <= 20) {
		status = "speeding";
		console.log(
			`The speed is ${difference} km/h faster than the allowed speed of ${speeds[area]} - ${status}`
		);
	} else if (difference <= 40) {
		status = "excessive speeding";
		console.log(
			`The speed is ${difference} km/h faster than the allowed speed of ${speeds[area]} - ${status}`
		);
	} else {
		status = "reckless driving";
		console.log(
			`The speed is ${difference} km/h faster than the allowed speed of ${speeds[area]} - ${status}`
		);
	}
}
 
roadRadar(55, "city");
