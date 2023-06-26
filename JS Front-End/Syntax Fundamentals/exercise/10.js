function sameNums(number) {
	let num = number.toString();
	let isSame = true;
	let firstDigit = num[0];
	let sum = 0;
	for (let i = 0; i < num.length; i++) {
		if (num[i] !== firstDigit) {
			isSame = false;
			sum += Number(num[i]);
		} else {
			sum += Number(num[i]);
		}
	}
	console.log(isSame);
	console.log(sum);
}

sameNums(2222222);
