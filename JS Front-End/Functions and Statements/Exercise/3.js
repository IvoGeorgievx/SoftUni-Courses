// console.log("a".charCodeAt(0));
// console.log("d".charCodeAt(0));
// console.log(String.fromCharCode(97));

function charsInRange(x, y) {
	resultArray = [];
	firstChar = x.charCodeAt(0);
	secondChar = y.charCodeAt(0);
	if (firstChar > secondChar) {
		for (let i = secondChar + 1; i < firstChar; i++) {
			let currentSymbol = String.fromCharCode(i);
			resultArray.push(currentSymbol);
		}
	} else {
		for (let i = firstChar + 1; i < secondChar; i++) {
			let currentSymbol = String.fromCharCode(i);
			resultArray.push(currentSymbol);
		}
	}

	return resultArray.join(" ");
}

console.log(charsInRange("#", ":"));


