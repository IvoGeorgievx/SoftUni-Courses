projection_type = input()
rows = int(input())
columns = int(input())

premiere = 12.00
normal = 7.50
discount = 5
income = 0

if projection_type == 'Premiere':
    income = rows * columns * premiere
elif projection_type == 'Normal':
    income = rows * columns * normal
elif projection_type == 'Discount':
    income = rows * columns * discount
print(f'{income:.2f}')

