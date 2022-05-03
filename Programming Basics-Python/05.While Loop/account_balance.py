total_amount = 0
amount = input()

while amount != 'NoMoreMoney':
    current_number = float(amount)
    if current_number < 0:
        print('Invalid operation!')
        break
    total_amount += current_number
    print(f'Increase: {current_number:.2f}')
    amount = input()
print(f'Total: {total_amount:.2f}')





