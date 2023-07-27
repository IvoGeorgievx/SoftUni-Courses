function attachEvents() {
	const button = document.querySelector("#submit");
	button.addEventListener("click", () => {
		const location = document.querySelector("#location").value;

		fetch("http://localhost:3030/jsonstore/forecaster/locations")
			.then((res) => res.json())
			.then((body) => {
				const currentCity = body.find((loc) => loc.name === location);
				const displayDiv = document.querySelector("#forecast");
				displayDiv.style.display = "block";
				currentConditions(currentCity.code);
				forecastConditions(currentCity.code);
			})
			.catch(() => {
				const displayDiv = document.querySelector("#forecast");
				displayDiv.style.display = "block";
				displayDiv.innerHTML = "Error";
			});
	});

	function currentConditions(cityCode) {
		fetch(`http://localhost:3030/jsonstore/forecaster/today/${cityCode}`)
			.then((res) => res.json())
			.then((data) => {
				const parentDiv = document.querySelector("#current");
				const forecastDiv = document.createElement("div");
				forecastDiv.classList.add("forecasts");
				appendForecastChilds(parentDiv, forecastDiv);

				const conditionSpan = document.createElement("span");
				conditionSpan.classList.add("condition");

				const symbolSpan = document.createElement("span");
				symbolSpan.classList.add("condition", "symbol");
				symbolSpan.innerHTML = "☀";

				appendForecastChilds(forecastDiv, symbolSpan, conditionSpan);

				const forecastCity = document.createElement("span");
				forecastCity.classList.add("forecast-data");
				forecastCity.innerHTML = data.name;

				const temperature = createUpcomingTemp(data);

				const condition = document.createElement("span");
				condition.classList.add("forecast-data");
				condition.innerHTML = data.forecast.condition;

				appendForecastChilds(
					conditionSpan,
					forecastCity,
					temperature,
					condition
				);
			});
	}

	function forecastConditions(cityCode) {
		fetch(`http://localhost:3030/jsonstore/forecaster/upcoming/${cityCode}`)
			.then((res) => res.json())
			.then((data) => {
				const upcomingDiv = document.querySelector("#upcoming");
				const forecastInfoDiv = document.createElement("div");
				forecastInfoDiv.classList.add("forecast-info");

				const upcomingSpan = createUpcomingSpan();

				appendForecastChilds(upcomingDiv, forecastInfoDiv);

				const upcomingSymbolSpan = createWeatherSymbol("⛅");

				const upcomingTemp = document.createElement("span");
				upcomingTemp.classList.add("forecast-data");
				upcomingTemp.innerHTML = `${data.forecast[0].low}°/${data.forecast[0].high}°`;

				const upcomingCondition = document.createElement("span");
				upcomingCondition.classList.add("forecast-data");
				upcomingCondition.innerHTML = data.forecast[0].condition;

				const upcomingSymbolSpan1 = createWeatherSymbol("☁");

				const upcomingSpan1 = createUpcomingSpan();

				const upcomingTemp1 = document.createElement("span");
				upcomingTemp1.classList.add("forecast-data");
				upcomingTemp1.innerHTML = `${data.forecast[1].low}°/${data.forecast[1].high}°`;

				const upcomingCondition1 = document.createElement("span");
				upcomingCondition1.classList.add("forecast-data");
				upcomingCondition1.innerHTML = data.forecast[1].condition;

				const upcomingSymbolSpan2 = createWeatherSymbol("☁");

				const upcomingSpan2 = createUpcomingSpan();

				const upcomingTemp2 = document.createElement("span");
				upcomingTemp2.classList.add("forecast-data");
				upcomingTemp2.innerHTML = `${data.forecast[2].low}°/${data.forecast[2].high}°`;

				const upcomingCondition2 = document.createElement("span");
				upcomingCondition2.classList.add("forecast-data");
				upcomingCondition2.innerHTML = data.forecast[2].condition;

				appendForecastChilds(forecastInfoDiv, upcomingSpan);
				appendForecastChilds(
					upcomingSpan,
					upcomingSymbolSpan,
					upcomingTemp,
					upcomingCondition
				);

				appendForecastChilds(forecastInfoDiv, upcomingSpan1);
				appendForecastChilds(
					upcomingSpan1,
					upcomingCondition1,
					upcomingSymbolSpan1,
					upcomingTemp1,
					upcomingCondition1
				);

				appendForecastChilds(forecastInfoDiv, upcomingSpan2);
				appendForecastChilds(
					upcomingSpan2,
					upcomingCondition2,
					upcomingSymbolSpan2,
					upcomingTemp2,
					upcomingCondition2
				);
			});
	}

	function createWeatherSymbol(symbol) {
		const weatherSymbol = document.createElement("span");
		weatherSymbol.classList.add("symbol");
		weatherSymbol.innerHTML = symbol;

		return weatherSymbol;
	}

	function appendForecastChilds(parentDiv, ...args) {
		Array.from(args).forEach((element) => {
			parentDiv.appendChild(element);
		});
	}

	function createUpcomingTemp(data) {
		const temperature = document.createElement("span");
		temperature.classList.add("forecast-data");
		temperature.innerHTML = `${data.forecast.low}°/${data.forecast.high}°`;

		return temperature;
	}

	function createUpcomingSpan() {
		const upcomingSpan = document.createElement("span");
		upcomingSpan.classList.add("upcoming");

		return upcomingSpan;
	}
}

attachEvents();
