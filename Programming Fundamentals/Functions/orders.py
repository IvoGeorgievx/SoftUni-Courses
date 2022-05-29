def total_price(product, quantity):
    if product == 'coffee':
        return 1.50 * quantity
    elif product == 'water':
        return quantity * 1
    elif product == 'coke':
        return 1.40 * quantity
    elif product == 'snacks':
        return 2 * quantity


product = input()
quantity = int(input())
print(f'{total_price(product, quantity):.2f}')
