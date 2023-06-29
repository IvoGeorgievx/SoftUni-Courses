const subtract = (sum, num) => sum - num;

const addAndSubtract = (num1, num2, num3) => subtract(num1 + num2, num3);

function addAndSubtract1(num1, num2, num3) {
	const sum = num1 + num2;
	function sumSubtract(sum, number) {
		return sum - number;
	}
    return sumSubtract(sum, num3)
}

console.log(addAndSubtract(1, 17, 30));
console.log(addAndSubtract1(1, 17, 30));
