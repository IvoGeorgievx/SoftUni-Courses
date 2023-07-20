function addItem() {
	const textInput = document.querySelector("#newItemText");
	const valueInput = document.querySelector("#newItemValue");

	const menu = document.querySelector("#menu");

	const newOption = document.createElement("option");
	newOption.textContent = textInput.value;
	newOption.value = valueInput.value;
	menu.appendChild(newOption);
	textInput.value = "";
	valueInput.value = "";
}
