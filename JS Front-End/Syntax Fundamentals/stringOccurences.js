function stringOccurances(string, searchedWord) {
	let count = 0;
	let words = string.split(" ");
	for (let word of words) {
		if (word === searchedWord) {
			count++;
		}
	}
	console.log(count);
}

stringOccurances(
	"softuni is great place for learning new programming languages",
	"softuni"
);
