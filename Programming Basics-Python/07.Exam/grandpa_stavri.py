days = int(input())
litres_total = 0
degree_total = 0
for _ in range(days):
    rakija_quantity = float(input())
    rakija_degree = float(input())
    litres_total += rakija_quantity
    degree_total += rakija_degree * rakija_quantity
degree_average = degree_total / litres_total
print(f'Liter: {litres_total:.2f}')
print(f'Degrees: {degree_average:.2f}')
if degree_average < 38:
    print('Not good, you should baking!')
elif 38 <= degree_average <= 42:
    print('Super!')
elif degree_average > 42:
    print('Dilution with distilled water!')

