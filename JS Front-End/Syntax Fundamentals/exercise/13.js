function arrayRotation(array, num) {
    for (let i = 0; i < num; i++) {
        let firstElement = array.shift()
        array.push(firstElement)
    }
    console.log(array.join(' '));
}

arrayRotation([32, 21, 61, 1], 4)