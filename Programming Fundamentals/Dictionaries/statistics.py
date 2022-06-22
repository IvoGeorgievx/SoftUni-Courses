command = input()
products = {}

while command != 'statistics':
    exploded = command.split(": ")
    product = exploded[0]
    quantity = int(exploded[1])

    if product not in products.keys():
        products[product] = quantity
    else:
        products[product] += quantity

    command = input()

count = len(products.keys())
total = sum(products.values())

print("Products in stock:")
for product in products:
    print(f"- {product}: {products[product]}")
print(f"Total Products: {count}")
print(f"Total Quantity: {total}")


