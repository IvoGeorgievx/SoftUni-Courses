function toggle() {
	const button = document.querySelector(".button");
	const hiddenDiv = document.querySelector("#extra");

	hiddenDiv.style.display =
		hiddenDiv.style.display === "block" ? "none" : "block";
	button.textContent = button.textContent === "Less" ? "More" : "Less";

	// if (hiddenDiv.style.display !== "block") {
	// 	hiddenDiv.style.display = "block";
	// 	button.textContent = 'Less'
	// } else {
	// 	hiddenDiv.style.display = "none";
	// 	button.textContent = 'More'
	// }
}
