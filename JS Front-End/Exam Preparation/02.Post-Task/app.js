window.addEventListener("load", solve);

function solve() {
	const publishButton = document.querySelector("#publish-btn");
	publishButton.addEventListener("click", publish);

	function publish() {
		const taskTitle = document.querySelector("#task-title");
		const taskDescription = document.querySelector("#task-category");
		const taskContent = document.querySelector("#task-content");

		if (
			taskTitle.value.trim() === "" ||
			taskDescription.value.trim() === "" ||
			taskContent.value.trim() === ""
		) {
			return;
		}

		const neededUl = document.querySelector("#review-list");

		const li = document.createElement("li");
		li.classList.add("rpost");

		const article = document.createElement("article");
		const h4 = document.createElement("h4");
		h4.textContent = taskTitle.value;
		const p1 = document.createElement("p");
		p1.textContent = `Category: ${taskDescription.value}`;
		const p1Value = taskDescription.value;
		const p2 = document.createElement("p");
		const p2Value = taskContent.value;
		p2.textContent = `Content: ${taskContent.value}`;

		const editButton = document.createElement("button");
		editButton.innerHTML = "Edit";
		editButton.classList.add("action-btn", "edit");
		editButton.addEventListener("click", editFunction);

		const postButton = document.createElement("button");
		postButton.innerHTML = "Post";
		postButton.classList.add("action-btn", "post");
		postButton.addEventListener("click", postFunction);

		article.appendChild(h4);
		article.appendChild(p1);
		article.appendChild(p2);
		li.appendChild(article);
		li.appendChild(editButton);
		li.appendChild(postButton);
		neededUl.appendChild(li);

		taskTitle.value = "";
		taskDescription.value = "";
		taskContent.value = "";

		function editFunction() {
			neededUl.removeChild(li);
			taskTitle.value = h4.textContent;
			taskDescription.value = p1Value;
			taskContent.value = p2Value;
		}

		function postFunction() {
			const publishedUl = document.querySelector("#published-list");
			neededUl.removeChild(li);
			li.removeChild(editButton);
			li.removeChild(postButton);
			publishedUl.appendChild(li);
		}
	}
}
