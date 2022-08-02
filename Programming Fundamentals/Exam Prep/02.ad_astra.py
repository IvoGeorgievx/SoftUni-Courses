import re
from math import floor

info = input()

pattern = r'([#|])([a-zA-Z]+ ?[a-zA-Z]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
result = re.finditer(pattern, info)
total_calories = 0

for resul in result:
    total_calories += int(resul[4])

food_total = floor(total_calories / 2000)

print(f'You have food to last you for: {food_total} days!')
pattern1 = r'([#|])([a-zA-Z]+ ?[a-zA-Z]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
result1 = re.finditer(pattern1, info)

for resul in result1:
    print(f"Item: {resul[2]}, Best before: {resul[3]}, Nutrition: {resul[4]}")
