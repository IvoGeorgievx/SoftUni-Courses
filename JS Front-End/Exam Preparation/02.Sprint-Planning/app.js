window.addEventListener("load", solve);

function solve() {
	const inputSelectors = {
		title: document.querySelector("#title"),
		description: document.querySelector("#description"),
		asignee: document.querySelector("#assignee"),
		label: document.querySelector("#label"),
		points: document.querySelector("#points"),
	};

	const buttons = {
		createTask: document.querySelector("#create-task-btn"),
		deleteTask: document.querySelector("#delete-task-btn"),
	};

	const icons = {
		feature: "&#8865",
		"Low Priority Bug": "&#9737",
		"High Priority Bug": "&#9888",
	};

	const classLabels = {
		feature: "feature",
		"low priority bug": "low-priority",
		"high priority bug": "high-priority",
	};

	buttons.createTask.addEventListener("click", createTask);

	function createTask() {
		if (Object.values(inputSelectors).some((input) => input.value === "")) {
			return;
		}
	}
}
