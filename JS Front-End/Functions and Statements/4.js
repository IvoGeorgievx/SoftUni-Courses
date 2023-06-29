function orders(product, quantity) {
    prices = {
        "coffee": 1.5,
        "water": 1,
        "coke": 1.4,
        "snacks": 2
    }
    return (prices[product] * quantity).toFixed(2)
}

console.log(orders("coffee", 2))