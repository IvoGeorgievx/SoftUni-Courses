budget = int(input())
season = input()
fishermen = int(input())

ship_rent = 0

if season == 'Spring':
    ship_rent = 3000
elif season == 'Summer':
    ship_rent = 4200
elif season == 'Autumn':
    ship_rent = 4200
elif season == 'Winter':
    ship_rent = 2600

if fishermen <= 6:
    ship_rent = ship_rent - (ship_rent * 0.1)
elif 7 <= fishermen <= 11:
    ship_rent = ship_rent - (ship_rent * 0.15)
elif fishermen >= 12:
    ship_rent = ship_rent - (ship_rent * 0.25)
elif fishermen % 2 == 0:
    ship_rent = ship_rent - (ship_rent * 0.05)

if budget > ship_rent:
    money_left = budget - ship_rent
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_left = budget - ship_rent
    print(f'Not enough money! You need {abs(money_left):.2f} leva.')




