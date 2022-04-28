age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_saved = 0
toys_count = 0
amount = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        amount += 10
        money_saved += amount - 1
    else:
        toys_count += 1
toy_amount = toy_price * toys_count
total_amount = toy_amount + money_saved
if total_amount < washing_machine_price:
    print(f'No! {washing_machine_price - total_amount:.2f}')
else:
    print(f'Yes! {total_amount - washing_machine_price:.2f}')


