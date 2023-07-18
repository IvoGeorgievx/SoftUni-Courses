function create(words) {
	words.forEach((word) => {
		const newDiv = document.createElement("div");
		const newParagraph = document.createElement("p");
		newParagraph.textContent = word;
		newParagraph.style.display = "none";
		newDiv.addEventListener("click", () => {
			newParagraph.style.display = "block";
		});

		newDiv.appendChild(newParagraph);
		const mainDiv = document.querySelector("#content");
		mainDiv.appendChild(newDiv);
	});
}
