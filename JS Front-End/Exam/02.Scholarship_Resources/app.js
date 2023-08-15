window.addEventListener("load", solve);

function solve() {
	const studentInput = document.querySelector("#student");
	const uniInput = document.querySelector("#university");
	const scoreInput = document.querySelector("#score");

	const nextBtn = document.querySelector("#next-btn");
	nextBtn.addEventListener("click", () => {
		if (
			studentInput.value === "" ||
			uniInput.value === "" ||
			scoreInput.value === ""
		) {
			return;
		}

		const studentInputTempValue = studentInput.value;
		const uniInputTempValue = uniInput.value;
		const scoreInputTempValue = scoreInput.value;

		const mainUl = document.querySelector("#preview-list");

		const mainLi = createElement("li", null, ["application"], null, mainUl);
		const mainArticle = createElement("article", null, ["info"], null, mainLi);
		createElement("h4", studentInput.value, null, null, mainArticle);
		createElement(
			"p",
			`University: ${uniInput.value}`,
			null,
			null,
			mainArticle
		);
		createElement("p", `Score: ${scoreInput.value}`, null, null, mainArticle);

		const editBtn = createElement(
			"button",
			"edit",
			["action-btn", "edit"],
			null,
			mainLi
		);
		const applyBtn = createElement(
			"button",
			"apply",
			["action-btn", "apply"],
			null,
			mainLi
		);

		scoreInput.value = "";
		uniInput.value = "";
		studentInput.value = "";
		nextBtn.disabled = true;

		editBtn.addEventListener("click", (e) => {
			studentInput.value = studentInputTempValue;
			uniInput.value = uniInputTempValue;
			scoreInput.value = scoreInputTempValue;
			nextBtn.disabled = false;
			mainLi.remove();
		});

		applyBtn.addEventListener("click", (e) => {
			mainLi.remove();
			const candidateUl = document.querySelector("#candidates-list");
			candidateUl.appendChild(mainLi);
			applyBtn.remove();
			editBtn.remove();
			nextBtn.disabled = false;
		});
	});

	function createElement(type, content, classes, id, parent) {
		const element = document.createElement(type);

		if (content) {
			element.textContent = content;
		}

		if (classes && classes.length > 0) {
			element.classList.add(...classes);
		}

		if (id) {
			element.setAttribute("id", id);
		}

		if (parent) {
			parent.appendChild(element);
		}
		return element;
	}
}
