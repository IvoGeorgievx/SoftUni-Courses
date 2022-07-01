def orders():
    command = input()
    basket = dict()

    while command != 'buy':
        data = command.split(" ")
        product = data[0]
        price = float(data[1])
        quantity = int(data[2])

        if product in basket:
            basket[product] = [price, (quantity + basket[product][1])]
        else:
            basket[product] = [price, quantity]

        command = input()

    for k in basket:
        total_sum = basket[k][0] * basket[k][1]
        print(f"{k} -> {total_sum:.2f}")


orders()