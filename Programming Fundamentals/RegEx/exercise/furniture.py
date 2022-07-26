import re

command = input()
pattern = r'>>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)'
new_list = []
spend_money = 0

while command != 'Purchase':

    result = re.match(pattern, command)
    if result is not None:
        item = result[1]
        price = float(result[2])
        quantity = float(result[3])
        spend_money += price * quantity
        new_list.append(item)

    command = input()

print('Bought furniture:')

if spend_money > 0:
    print('\n'.join(new_list))
print(f'Total money spend: {spend_money:.2f}')




