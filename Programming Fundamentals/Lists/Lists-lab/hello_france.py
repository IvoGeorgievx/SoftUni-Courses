items = input().split("|")
budget = int(input())
starting_budget = budget
profit_list = []
profit = 0
condition = False

for item in items:
    current_item = item.split("->")
    item_type = current_item[0]
    item_price = float(current_item[1])
    condition = False
    if item_type == 'Clothes' and item_price <= 50:
        condition = True
    elif item_type == 'Shoes' and item_price <= 35:
        condition = True
    elif item_type == 'Accessories' and item_price <= 20.50:
        condition = True
    if condition:
        if budget < item_price:
            break
        budget -= item_price
        new_item_price = item_price + (item_price * 0.4)
        profit += new_item_price - item_price
        profit_list.append(f'{new_item_price:.2f}')

print(' '.join(profit_list))
print(f'Profit: {profit:.2f}')
if starting_budget + profit >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')

