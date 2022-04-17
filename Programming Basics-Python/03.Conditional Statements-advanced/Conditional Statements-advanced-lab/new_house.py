flower_type = input()
flower_count = int(input())
budget = int(input())
price = 0


if flower_type == 'Roses':
    price = 5
    if flower_count > 80:
        price = price - (price * 0.1)
elif flower_type == 'Dahlias':
    price = 3.80
    if flower_count > 90:
        price = price - (price * 0.15)
elif flower_type == 'Tulips':
    price = 2.80
    if flower_count > 80:
        price = price - (price * 0.15)
elif flower_type == 'Narcissus':
    price = 3
    if flower_count < 120:
        price = price + (price * 0.15)
elif flower_type == 'Gladiolus':
    price = 2.50
    if flower_count < 80:
        price = price + (price * 0.2)
total_cost = price * flower_count

if total_cost > budget:
    required_amount = total_cost - budget
    print(f'Not enough money, you need {abs(required_amount):.2f} leva more.')
else:
    amount_left = budget - total_cost
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {amount_left:.2f} leva left.')











