def cost(product, city):
    if city == 'Sofia' and product == 'coffee':
        price = 0.50
    elif city == 'Sofia' and product == 'water':
        price = 0.80
    elif city == 'Sofia' and product == 'beer':
        price = 1.20
    elif city == 'Sofia' and product == 'sweets':
        price = 1.45
    elif city == 'Sofia' and product == 'peanuts':
        price = 1.60
    if city == 'Plovdiv' and product == 'coffee':
        price = 0.40
    elif city == 'Plovdiv' and product == 'water':
        price = 0.70
    elif city == 'Plovdiv' and product == 'beer':
        price = 1.15
    elif city == 'Plovdiv' and product == 'sweets':
        price = 1.30
    elif city == 'Plovdiv' and product == 'peanuts':
        price = 1.50

    if city == 'Varna' and product == 'coffee':
        price = 0.45
    elif city == 'Varna' and product == 'water':
        price = 0.70
    elif city == 'Varna' and product == 'beer':
        price = 1.10
    elif city == 'Varna' and product == 'sweets':
        price = 1.35
    elif city == 'Varna' and product == 'peanuts':
        price = 1.55
    return price * quantity


product = input()
city = input()
quantity = float(input())
print(f'{cost(product, city):.2f}')
