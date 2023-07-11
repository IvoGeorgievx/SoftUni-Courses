function towns(array) {
	const result = array.map((element) => {
		return element.split(" | ");
	});

	const array1 = result.forEach((values) => {
		const [name, latitude, longitude] = values;
		return console.log({
			town: name,
			latitude: Number(latitude).toFixed(2),
			longitude: Number(longitude).toFixed(2),
		});
	});
}

towns(["Sofia | 42.696552 | 23.32601", "Beijing | 39.913818 | 116.363625"]);
