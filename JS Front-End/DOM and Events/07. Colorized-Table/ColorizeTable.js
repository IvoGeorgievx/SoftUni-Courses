function colorize() {
	const neededRows = Array.from(
		document.querySelectorAll("tr:nth-child(even)")
	);
	console.log(neededRows);

	neededRows.forEach((row) => {
		row.style.backgroundColor = "teal";
	});
}
