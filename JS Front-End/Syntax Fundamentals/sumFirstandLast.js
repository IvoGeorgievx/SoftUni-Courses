function sumFirstandLast(arr) {
	let first = Number(arr.shift());
	let last = Number(arr.pop());
	return console.log(first + last);
}

sumFirstandLast([20, 30, 40]);
