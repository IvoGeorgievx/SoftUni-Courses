function getInfo() {
	const stopId = document.querySelector("#stopId").value;
	const ul = document.querySelector("#buses");
	const stopName = document.querySelector("#stopName");

	fetch(`http://localhost:3030/jsonstore/bus/businfo/${stopId}`)
		.then((res) => res.json())
		.catch(customError)
		.then((data) => parseData(data))
		.catch(customError);

	function customError() {
		stopName.textContent = "Error";
		ul.innerHTML = "";
	}

	function parseData(data) {
		stopName.textContent = data.name;
		Object.keys(data.buses).forEach((busNumber) => {
			const time = data.buses[busNumber];
			const li = document.createElement("li");
			li.textContent = `Bus ${busNumber} : ${time} minutes`;
			ul.appendChild(li);
		});
	}
}
