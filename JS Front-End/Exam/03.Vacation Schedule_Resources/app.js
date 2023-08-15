const API_URL = "http://localhost:3030/jsonstore/tasks/";

const loadBtn = document.querySelector("#load-vacations");

loadBtn.addEventListener("click", loadData);

const addVacationBtn = document.querySelector("#add-vacation");

addVacationBtn.addEventListener("click", addVacation);

const bigEditButton = document.querySelector("#edit-vacation");

const mainDiv = document.querySelector("#list");

const inputs = {
	name: document.querySelector("#name"),
	days: document.querySelector("#num-days"),
	date: document.querySelector("#from-date"),
};

async function loadData() {
	mainDiv.innerHTML = "";

	const response = await (await fetch(API_URL)).json();

	Object.values(response).forEach((vacation) => {
		// console.log(vacation._id);
		const containerDiv = createElement(
			"div",
			null,
			["container"],
			null,
			mainDiv
		);

		createElement("h2", vacation.name, [], null, containerDiv);
		createElement("h3", vacation.date, [], null, containerDiv);
		createElement("h3", vacation.days, [], null, containerDiv);
		const changeBtn = createElement(
			"button",
			"Change",
			["change-btn"],
			null,
			containerDiv
		);

		changeBtn.addEventListener("click", async (e) => {
			e.preventDefault();
			addVacationBtn.disabled = true;
			bigEditButton.disabled = false;

			inputs.name.value = vacation.name;
			inputs.days.value = vacation.days;
			inputs.date.value = vacation.date;
			containerDiv.remove();

			bigEditButton.addEventListener("click", async (e) => {
				e.preventDefault();

				const updatedVacation = {
					_id: vacation._id,
					name: inputs.name.value,
					days: inputs.days.value,
					date: inputs.date.value,
				};
				await (
					await fetch(API_URL + vacation._id, {
						method: "PUT",
						body: JSON.stringify(updatedVacation),
					})
				).json();
				await loadData();
				addVacationBtn.disabled = false;
				bigEditButton.disabled = true;

				inputs.name.value = "";
				inputs.days.value = "";
				inputs.date.value = "";
			});
		});

		const doneBtn = createElement(
			"button",
			"Done",
			["done-btn"],
			null,
			containerDiv
		);
		doneBtn.addEventListener("click", async (e) => {
			e.preventDefault();
			const id = vacation._id;
			console.log(id);
			await (
				await fetch(API_URL + vacation._id, {
					method: "DELETE",
				})
			).json();
			containerDiv.remove();
			await loadData();
		});
	});
}

async function addVacation(e) {
	e.preventDefault();
	if (
		inputs.name.value === "" ||
		inputs.date.value === "" ||
		inputs.days.value === ""
	) {
		return;
	}

	const vacation = {
		name: inputs.name.value,
		days: inputs.days.value,
		date: inputs.date.value,
	};

	const response = await fetch(API_URL, {
		method: "POST",
		body: JSON.stringify(vacation),
	});

	const newVacation = await response.json();
	vacation._id = newVacation._id;

	await loadData();

	inputs.name.value = "";
	inputs.days.value = "";
	inputs.date.value = "";
}

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
