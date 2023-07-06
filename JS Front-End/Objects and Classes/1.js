function personInfo(firstName, lastName, age) {
	let person = {};
	person.firstName = firstName;
	person.lastName = lastName;
	person.age = age;
	console.log(`firstName: ${person.firstName}`);
	console.log(`lastName: ${person.lastName}`);
	console.log(`age: ${person.age}`);
}

personInfo("Ivo", "Georgiev", 29);
