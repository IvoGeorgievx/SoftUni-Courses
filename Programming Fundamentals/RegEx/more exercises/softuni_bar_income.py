import re

pattern = r'%([A-Z][a-z]+)%<([a-zA-Z0-9]+)>\|([0-9]+)\|([0-9]+\.[0-9]+)\$'
total_income = 0

while True:
    products = input()

    if products == 'end of shift':
        break

    result = re.match(pattern, products)

    if result is not None:
        name = result[1]
        item = result[2]
        counter = int(result[3])
        price = float(result[4])
        total_price = counter * price
        print(f'{name}: {item} - {total_price:.2f}')
        total_income += total_price

print(f'Total income: {total_income:.2f}')


