function addItem() {
	const value1 = document.querySelector("#newItemText").value;
	const item = document.createElement("li");
	item.textContent = value1;

	document.querySelector("ul").appendChild(item);
}
