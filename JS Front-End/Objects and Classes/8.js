function addressBook(array) {
	finalObject = array.reduce((acc, curr) => {
		const [name, street] = curr.split(":");
		acc[name] = street;
		return acc;
	}, {});
    const sortedKeys = Object.entries(finalObject).sort()
	for (let [key, value] of sortedKeys) {
        console.log(`${key} -> ${value}`);
    }
}

addressBook([
	"Tim:Doe Crossing",
	"Bill:Nelson Place",
	"Peter:Carlyle Ave",
	"Bill:Ornery Rd",
]);
