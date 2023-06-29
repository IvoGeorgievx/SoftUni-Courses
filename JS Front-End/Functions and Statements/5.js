const operations = {
	add: (x, y) => x + y,
	subtract: (x, y) => x - y,
	multiply: (x, y) => x * y,
	devide: (x, y) => x / y,
};

const calculator = (x, y, operation) => operations[operation](x, y);

console.log(calculator(5, 5, "multiply"));
