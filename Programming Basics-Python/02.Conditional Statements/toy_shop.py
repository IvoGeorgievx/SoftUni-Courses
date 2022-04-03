trip_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

income = number_of_puzzles * puzzle + number_of_dolls * talking_doll \
    + number_of_bears * teddy_bear + number_of_minions * minion + number_of_trucks * truck
number_of_toys = number_of_trucks + number_of_minions + number_of_bears + number_of_puzzles + number_of_dolls
if number_of_toys >= 50:
    income = income - (income * 0.25)
rent = income * 0.1
profit = income - rent

if profit >= trip_price:
   profit = profit - trip_price
   print(f'Yes! {profit:.2f} lv left.')
elif trip_price > profit:
    profit = profit - trip_price
    aprofit = abs(profit)
    print(f'Not enough money! {aprofit:.2f} lv needed.')













