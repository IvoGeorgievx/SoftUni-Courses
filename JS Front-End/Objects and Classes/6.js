function phoneBook(arr) {
	const phoneOjb = arr.reduce((acc, curr) => {
		const [name, phone] = curr.split(" ");
        acc[name] = phone
        return acc
	}, {});

    Object.keys(phoneOjb).forEach((key) => {
        console.log(`${key} -> ${phoneOjb[key]}`);
    })
}

phoneBook([
	"Tim 0834212554",
	"Peter 0877547887",
	"Bill 0896543112",
	"Tim 0876566344",
]);
