from math import floor
from math import ceil
days_gone = int(input())
food_left_total = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food_grams = float(input())

turtle_food_kg = turtle_food_grams / 1000
pet_food_total = (dog_food + cat_food + turtle_food_kg) * days_gone

if pet_food_total <= food_left_total:
    print(f'{floor(food_left_total - pet_food_total)} kilos of food left.')
else:
    print(f'{ceil(pet_food_total - food_left_total)} more kilos of food are needed.')


