function numsSum(num1, num2) {
	let sum = 0;
	let numsArray = [];
	for (let i = num1; i <= num2; i++) {
		sum += i;
		numsArray.push(i);
	}
	console.log(numsArray.join(" "));
	console.log(`Sum: ${sum}`);
}

numsSum(5, 10);
