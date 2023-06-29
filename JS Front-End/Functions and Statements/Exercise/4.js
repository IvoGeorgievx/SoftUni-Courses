function oddAndEvenSum(numString) {
	let oddSum = 0;
	let evenSum = 0;
	for (let i = 0; i < numString.length; i++) {
		let digit = parseInt(numString[i]);
		if (digit % 2 === 0) {
			evenSum += digit;
		} else {
			oddSum += digit;
		}
	}
	return `Odd sum = ${oddSum}, Even sum = ${evenSum}`;
}

console.log(oddAndEvenSum("1000435"));
