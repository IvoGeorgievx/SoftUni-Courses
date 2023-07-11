function movies(array) {
	const movieObj = {};

	array.forEach((element) => {
		if (element.includes("addMovie")) {
			const [, ...rest] = element.split(" ");
			const movieName = rest.join(" ");
			movieObj[movieName] = {};
		} else if (element.includes("directedBy")) {
			const movieName = element.split(" ")[0];
			if (movieObj.hasOwnProperty(movieName)) {
				const [, , ...director] = element.split(" ");
				movieObj[movieName]["director"] = director.join(" ");
			}
		} else if (element.includes("onDate")) {
			const movieName = element.split(" ")[0];
			if (movieObj.hasOwnProperty(movieName)) {
				const [, , ...date] = element.split(" ");
				movieObj[movieName]["date"] = date.join(" ");
			}
		}
	});

	return movieObj;
}

const result = movies([
	"addMovie Fast and Furious",
	"addMovie Godfather",
	"Inception directedBy Christopher Nolan",
	"Godfather directedBy Francis Ford Coppola",
	"Godfather onDate 29.07.2018",
	"Fast and Furious onDate 30.07.2018",
	"Batman onDate 01.08.2018",
	"Fast and Furious directedBy Rob Cohen",
]);
