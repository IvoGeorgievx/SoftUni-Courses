# ⦁	Ако числото е до 100 включително, бонус точките са 5;
# ⦁	Ако числото е по-голямо от 100, бонус точките са 20% от числото;
# ⦁	Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
# ⦁	За четно число  + 1 т.
# ⦁	За число, което завършва на 5  + 2 т.

number = int(input())
bonus = 0

if number <= 100:
    bonus = 5
elif 100 < number <= 1000:
    bonus = number * 0.2
elif number > 1000:
    bonus = number * 0.1

if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2
total = number + bonus
print(bonus, total)
