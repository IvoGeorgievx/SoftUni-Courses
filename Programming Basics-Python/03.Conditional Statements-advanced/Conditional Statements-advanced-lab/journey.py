budget = float(input())
season = input()
sleep_location = ''
budget_spent = 0
country = ''

if budget <= 100 and season == 'summer':
    budget_spent = budget - (budget * 0.3)
elif budget <= 100 and season == 'winter':
    budget_spent = budget - (budget * 0.7)
if 100 < budget <= 1000 and season == 'summer':
    budget_spent = budget - (budget * 0.4)
elif 100 < budget <= 1000 and season == 'winter':
    budget_spent = budget - (budget * 0.8)
if budget > 1000 and season == 'summer':
    budget_spent = budget - (budget * 0.9)
elif budget > 1000 and season == 'winter':
    budget_spent = budget - (budget * 0.9)
budget_left = budget - budget_spent

if budget <= 100 and season == 'summer':
    print('Somewhere in Bulgaria')
    print(f'Camp - {budget - budget_spent:.2f}')
elif budget <= 100 and season == 'winter':
    print('Somewhere in Bulgaria')
    print(f'Hotel - {budget - budget_spent:.2f}')
if 100 < budget <= 1000 and season == 'summer':
    print('Somewhere in Balkans')
    print(f'Camp - {budget_left:.2f}')
elif 100 < budget <= 1000 and season == 'winter':
    print('Somewhere in Balkans')
    print(f'Hotel - {budget_left:.2f}')
if budget > 1000:
    print('Somewhere in Europe')
    print(f'Hotel - {budget_left:.2f}')

