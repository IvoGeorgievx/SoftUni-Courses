function lockedProfile() {
	const showMoreButtons = Array.from(document.querySelectorAll("button"));
	showMoreButtons.forEach((button) => {
		button.addEventListener("click", handleClick);
	});
}

function handleClick(e) {
    console.log(e);
	const lockedRadioButton = e.currentTarget.parentElement.querySelector(
		'input[type="radio"]'
	);
	if (lockedRadioButton.checked) {
		return;
	}

	const isHidden = e.currentTarget.textContent === "Show more";
	const hiddenInfo = e.currentTarget.parentElement.querySelector("div");

	hiddenInfo.style.display = isHidden ? "block" : "none";
	e.currentTarget.textContent = isHidden ? "Hide it" : "Show more";
}