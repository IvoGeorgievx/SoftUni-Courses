function charsInRange1(x, y) {
	const resultArray = [];
	const minChar = Math.min(x.charCodeAt(0), y.charCodeAt(0));
	const maxChar = Math.max(x.charCodeAt(0), y.charCodeAt(0));

	for (let i = minChar + 1; i < maxChar; i++) {
		let currentSymbol = String.fromCharCode(i);
		resultArray.push(currentSymbol);
	}

	return resultArray.join(" ");
}

console.log(charsInRange1("a", "d"));
