money_inherited = float(input())
present_year = int(input())

even_year_total = 0
odd_year_total = 0
odd_birthday_year = 17
total_spending = 0

for birthday in range(1800, present_year + 1):
    if birthday % 2 == 0:
        even_year_total += 12000
    elif birthday % 2 != 0:
        odd_birthday_year += 2
        odd_year_total += 12000 + 50 * odd_birthday_year
total_spending = even_year_total + odd_year_total

if money_inherited >= total_spending:
    print(f'Yes! He will live a carefree life and will have {money_inherited - total_spending:.2f} dollars left.')
else:
    print(f'He will need {abs(money_inherited - total_spending):.2f} dollars to survive.')

