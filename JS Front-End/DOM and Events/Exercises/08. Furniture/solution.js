function solve() {
	const button = document.querySelector("#exercise button");
	button.addEventListener("click", parseFurnitureInput);

	const buyButton = document.querySelector("#exercise button:last-child");
	buyButton.addEventListener("click", buySelectedFurniture);

	Array.from(document.querySelectorAll('input[type="checkbox"]')).forEach(
		(checkbox) => checkbox.removeAttribute("disabled")
	);
	function buySelectedFurniture() {
		const checkboxes = Array.from(
			document.querySelectorAll('input[type="checkbox"]:checked')
		);
		const cart = checkboxes
			.map((checkbox) => {
				const row = checkbox.parentElement.parentElement;
				const name = row.querySelector("td:nth-of-type(2)").innerText;
				const price = Number(row.querySelector("td:nth-of-type(3)").innerText);
				const decFactor = Number(
					row.querySelector("td:nth-of-type(4)").innerText
				);

				return { name, price, decFactor };
			})
			.reduce(
				(acc, curr) => {
					acc.names.push(curr.name);
					acc.price += Number(curr.price);
					acc.averageDecorationFactor += curr.decFactor;

					return acc;
				},
				{
					names: [],
					price: 0,
					averageDecorationFactor: 0,
				}
			);

		cart.averageDecorationFactor =
			cart.averageDecorationFactor / cart.names.length;

		const cartTextArea = document.querySelector(
			"#exercise textarea:nth-of-type(2)"
		);

		cartTextArea.value = `Bought furniture: ${cart.names.join(
			", "
		)} \nTotal price: ${cart.price.toFixed(
			2
		)} \nAvg Dec Factor: ${cart.averageDecorationFactor.toFixed(2)}
    `.trim();
	}

	function parseFurnitureInput() {
		const input = JSON.parse(
			document.querySelector("#exercise textarea").value
		);
		const tableBody = document.querySelector("tbody");

		input
			.map((furniture) => {
				const row = document.createElement("tr");

				const imageCell = document.createElement("td");
				const image = document.createElement("img");
				image.src = furniture.img;
				imageCell.appendChild(image);

				const nameCell = document.createElement("td");
				nameCell.textContent = furniture.name;

				const price = document.createElement("td");
				price.textContent = furniture.price;

				const decFactor = document.createElement("td");
				decFactor.textContent = furniture.decFactor;

				const checkCell = document.createElement("td");
				const checkbox = document.createElement("input");
				checkbox.type = "checkbox";
				checkCell.appendChild(checkbox);

				row.appendChild(imageCell);
				row.appendChild(nameCell);
				row.appendChild(price);
				row.appendChild(decFactor);
				row.appendChild(checkCell);

				return row;
			})
			.forEach((row) => {
				tableBody.appendChild(row);
			});
	}
}
