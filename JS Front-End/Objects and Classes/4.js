function convertToObject(jsonStr) {
	let person = JSON.parse(jsonStr);
	for (const [key, value] of Object.entries(person)) {
		console.log(`${key}: ${value}`);
	}
}

const jsontest = '{"name": "George", "age": 40, "town": "Sofia"}';
convertToObject(jsontest);
