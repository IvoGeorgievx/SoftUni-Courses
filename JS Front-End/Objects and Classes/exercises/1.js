function employees(input) {
	const employee = input.reduce((acc, curr) => {
		acc[curr] = curr.length;
		return acc;
	}, {});
    
    Object.keys(employee).forEach((key) => {
        console.log(`Name: ${key} -- Personal Number: ${employee[key]}`);
    })
}

employees([
	"Silas Butler",
	"Adnaan Buckley",
	"Juan Peterson",
	"Brendan Villarreal",
]);
