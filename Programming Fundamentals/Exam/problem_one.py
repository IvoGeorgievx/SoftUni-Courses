from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())

flour_count = 0

total_apron_price = (single_apron_price * ceil(students + (students * 0.2)))
eggs_total = single_egg_price * 10 * students

total_flour = 0

for flour in range(1, students + 1):
    if flour % 5 != 0:
        flour_count += 1
    total_flour = flour_count * flour_price

total = total_flour + eggs_total + total_apron_price

if total <= budget:
    print(f"Items purchased for {total:.2f}$.")
else:
    diff = abs(total - budget)
    print(f"{diff:.2f}$ more needed.")

