function vacation(group, type, day) {
	let sum = 0;
	const prices = {
		Students: {
			Friday: 8.45,
			Saturday: 9.8,
			Sunday: 10.46,
		},
		Business: {
			Friday: 10.9,
			Saturday: 15.6,
			Sunday: 16,
		},
		Regular: {
			Friday: 15,
			Saturday: 20,
			Sunday: 22.5,
		},
	};

	let price = prices[type][day];
	if (type === "Students" && group >= 30) {
		price *= 0.85;
	} else if (type === "Business" && group >= 100) {
		group -= 10;
	} else if (type === "Regular" && group >= 10 && group <= 20) {
		price *= 0.95;
	}
	sum = group * price;
	console.log(`Total price: ${sum.toFixed(2)}`);
}

vacation(30, "Students", "Sunday");
