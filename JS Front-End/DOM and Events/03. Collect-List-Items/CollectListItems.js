function extractText() {
	const items = Array.from(document.querySelectorAll("li"));
	const resultField = items.map((item) => item.textContent).join("\n");
	document.getElementById("result").value = resultField;
}
