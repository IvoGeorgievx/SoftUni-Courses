const repeatString = (string, num) => {
	if (num === 1) {
		return string;
	} else {
		return string + repeatString(string, num - 1);
	}
    
};

console.log(repeatString("String", 5));
