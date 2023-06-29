function signCheck(numOne, numTwo, numThree) {
	let negativeSign = 0;
	negativeSign += String(numOne).startsWith("-") ? 1 : 0;
	negativeSign += String(numTwo).startsWith("-") ? 1 : 0;
	negativeSign += String(numThree).startsWith("-") ? 1 : 0;
	return negativeSign === 1 || negativeSign === 3 ? "Negative" : "Positive";
}

console.log(signCheck(-6, -12, 14));
