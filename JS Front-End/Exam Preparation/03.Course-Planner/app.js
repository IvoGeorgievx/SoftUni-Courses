const API_URL = "http://localhost:3030/jsonstore/tasks/";

const loadCoursesBtn = document.querySelector("#load-course");
loadCoursesBtn.addEventListener("click", loadCourses);

const addButton = document.querySelector("#add-course");
addButton.addEventListener("click", addCourse);

const bigEditButton = document.querySelector("#edit-course");

const inputs = {
	title: document.querySelector("#course-name"),
	type: document.querySelector("#course-type"),
	description: document.querySelector("#description"),
	teacher: document.querySelector("#teacher-name"),
};

async function loadCourses() {
	const response = await (await fetch(API_URL)).json();

	const mainContainer = document.querySelector("#list");
	mainContainer.innerHTML = "";
	Object.values(response).forEach((course) => {
		const containerDiv = createElement(
			"div",
			null,
			["container"],
			null,
			mainContainer
		);
		createElement("h2", course.title, null, null, containerDiv);
		createElement("h3", course.teacher, null, null, containerDiv);
		createElement("h3", course.type, null, null, containerDiv);
		createElement("h4", course.description, null, null, containerDiv);
		const editCourseFromListButton = createElement(
			"button",
			"Edit Course",
			["edit-btn"],
			null,
			containerDiv
		);

		editCourseFromListButton.addEventListener("click", async (e) => {
			e.preventDefault();
			containerDiv.remove();

			inputs.title.value = course.title;
			inputs.teacher.value = course.teacher;
			inputs.type.value = course.type;
			inputs.description.value = course.description;

			bigEditButton.disabled = false;
			addButton.disabled = true;

			bigEditButton.addEventListener("click", async (e) => {
				e.preventDefault();
				if (
					inputs.type.value.trim() !== "Long" &&
					inputs.type.value.trim() !== "Short" &&
					inputs.type.value.trim() !== "Medium"
				) {
					return;
				}
				const newCourse = {
					title: inputs.title.value,
					teacher: inputs.teacher.value,
					type: inputs.type.value,
					description: inputs.description.value,
					_id: course._id,
				};
				await (
					await fetch(API_URL + course._id, {
						method: "PUT",
						body: JSON.stringify(newCourse),
					})
				).json();

				inputs.title.value = "";
				inputs.teacher.value = "";
				inputs.type.value = "";
				inputs.description.value = "";

				bigEditButton.disabled = true;
				addButton.disabled = false;

				await loadCourses();
			});
		});

		const finishCourseButton = createElement(
			"button",
			"Finish Course",
			["finish-btn"],
			null,
			containerDiv
		);

		finishCourseButton.addEventListener("click", async (e) => {
			e.preventDefault();
			await (await fetch(API_URL + course._id, { method: "DELETE" })).json();
			containerDiv.remove();
			await loadCourses();
		});
	});
}

async function addCourse(e) {
	e.preventDefault();

	if (areInputsEmptyWithSpaces(inputs)) {
		return;
	}
	if (
		inputs.type.value.trim() !== "Long" &&
		inputs.type.value.trim() !== "Short" &&
		inputs.type.value.trim() !== "Medium"
	) {
		return;
	}
	const newCourse = {
		title: inputs.title.value,
		teacher: inputs.teacher.value,
		type: inputs.type.value,
		description: inputs.description.value,
	};

	inputs.title.value = "";
	inputs.teacher.value = "";
	inputs.type.value = "";
	inputs.description.value = "";

	await (
		await fetch(API_URL, { method: "POST", body: JSON.stringify(newCourse) })
	).json();

	await loadCourses();
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

function areInputsEmptyWithSpaces(inputs) {
	return Object.values(inputs).some(
		(inputField) => inputField.value.trim() === ""
	);
}









