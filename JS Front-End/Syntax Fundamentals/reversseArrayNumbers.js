function reverseArray(num, array) {
	newArr = array.slice(0, num).reverse().join(" ");
	console.log(newArr);
}

reverseArray(4, [-1, 20, 99, 5]);
