budget = float(input())
category = input()
people_count = int(input())

vip_ticket = 499.99
normal_ticket = 249.99
ticket_price_total = 0
travel_expense = 0
budget_left = 0

if category == 'VIP':
    ticket_price_total = vip_ticket * people_count
elif category == 'Normal':
    ticket_price_total = normal_ticket * people_count
if 1 <= people_count <= 4:
    travel_expense = budget * 0.75
elif 5 <= people_count <= 9:
    travel_expense = budget * 0.6
elif 10 <= people_count <= 24:
    travel_expense = budget * 0.5
elif 25 <= people_count <= 49:
    travel_expense = budget * 0.4
elif people_count >= 50:
    travel_expense = budget * 0.25
budget_left = budget - travel_expense
money_left = budget_left - ticket_price_total

if 0 <= money_left:
    print(f'Yes! You have {budget_left - ticket_price_total:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(money_left):.2f} leva.')






