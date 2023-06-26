function fruits (fruit, weightGrams, pricePerKg) {
    let weightKg = weightGrams / 1000;
    let money = weightKg * pricePerKg;

    console.log(`I need $${money.toFixed(2)} to buy ${weightKg.toFixed(2)} kilograms ${fruit}.`);

}

fruits('orange', 2500, 1.80)