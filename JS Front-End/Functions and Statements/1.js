function gradeValue(x) {
	if (x < 3) {
		console.log(`Fail (2)`);
	} else if (x >= 3 && x < 3.5) {
		console.log(`Poor (${x.toFixed(2)})`);
	} else if (x >= 3.5 && x < 4.5) {
		console.log(`Good (${x.toFixed(2)})`);
	} else if (x >= 4.5 && x < 5.5) {
		console.log(`Very good (${x.toFixed(2)})`);
	} else if (x >= 5.5) {
		console.log(`Excellent (${x.toFixed(2)})`);
	}
}

const formatGrade = (grade, x) => {
	return grade(x);
};

formatGrade(gradeValue, 4.66);
