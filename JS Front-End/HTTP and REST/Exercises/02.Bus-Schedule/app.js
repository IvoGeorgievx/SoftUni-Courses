function solve() {
	const departButton = document.querySelector("#depart");
	const arriveButton = document.querySelector("#arrive");
	const resultField = document.querySelector("#info .info");

	let busStop = {
		name: "",
		next: "depot",
	};

	function depart() {
		fetch(`http://localhost:3030/jsonstore/bus/schedule/${busStop.next}`)
			.then((res) => res.json())
			.then((data) => {
				busStop = data;
				departButton.disabled = true;
				arriveButton.disabled = false;
				resultField.textContent = `Next stop ${busStop.name}`;
			})
			.catch(() => {
				departButton.disabled = true;
				arriveButton.disabled = true;
				resultField.textContent = "Error";
			});
	}

	async function arrive() {
		departButton.disabled = false;
		arriveButton.disabled = true;
		resultField.textContent = `Arriving at ${busStop.name}`;
	}

	return {
		depart,
		arrive,
	};
}

let result = solve();
