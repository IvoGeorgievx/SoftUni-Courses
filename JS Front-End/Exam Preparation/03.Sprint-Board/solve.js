const API_URL = "http://localhost:3030/jsonstore/tasks/";

function attachEvents() {
	let tasks = {};

	const loadButton = document.querySelector("#load-board-btn");
	loadButton.addEventListener("click", loadData);

	const addTaskButton = document.querySelector("#create-task-btn");
	addTaskButton.addEventListener("click", addTask);

	const articleSelectors = {
		ToDo: document.querySelector("#todo-section .task-list"),
		"In Progress": document.querySelector("#in-progress-section .task-list"),
		"Code Review": document.querySelector("#code-review-section .task-list"),
		Done: document.querySelector("#done-section .task-list"),
	};

	const buttonTextMap = {
		ToDo: "Move to In Progress",
		"In Progress": "Move to Code Review",
		"Code Review": "Move to Done",
		Done: "Close",
	};

	const statusToNextStatusMap = {
		ToDo: "In Progress",
		"In Progress": "Code Review",
		"Code Review": "Done",
		Done: "Close",
	};

	async function loadData() {
		tasks = await (await fetch(API_URL)).json();
		Object.values(articleSelectors).forEach(
			(article) => (article.textContent = "")
		);

		Object.values(tasks).forEach((task) => {
			const section = articleSelectors[task.status];
			const newLi = document.createElement("li");
			newLi.classList.add("task");
			const newH3 = document.createElement("h3");
			newH3.textContent = task.title;
			const newP = document.createElement("p");
			newP.textContent = task.description;
			const newButton = document.createElement("button");
			newButton.textContent = buttonTextMap[task.status];
			newButton.setAttribute("id", task._id);
			newButton.addEventListener("click", moveTask);

			newLi.appendChild(newH3);
			newLi.appendChild(newP);
			newLi.appendChild(newButton);
			section.appendChild(newLi);
		});
	}

	function addTask() {
		const inputs = {
			title: document.querySelector("#title"),
			description: document.querySelector("#description"),
		};

		if (Object.values(inputs).some((input) => input.value === "")) {
			return;
		}

		const task = {
			title: inputs.title.value,
			description: inputs.description.value,
			status: "ToDo",
		};

		fetch(API_URL, {
			method: "POST",
			body: JSON.stringify(task),
		});
		inputs.title.value = "";
		inputs.description.value = "";
		loadData();
	}

	async function moveTask(e) {
		const task = tasks[e.currentTarget.getAttribute("id")];
		let method = "PATCH";
		let body = JSON.stringify({
			...task,
			status: statusToNextStatusMap[task.status],
		});

		if (task.status === "Done") {
			method = "DELETE";
			body = undefined;
		}
		fetch(`${API_URL}/${task._id}`, {
			method,
			body,
		}).then(() => {
			loadData();
		});
	}
}

attachEvents();
