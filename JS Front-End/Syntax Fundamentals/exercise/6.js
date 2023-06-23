function sumNums(number) {
	let sum = 0;
	numArray = number.toString().split("");
	for (let i = 0; i < numArray.length; i++) {
		sum += Number(numArray[i]);
	}
    console.log(sum);
}

sumNums(245678)