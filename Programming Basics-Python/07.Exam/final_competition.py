dancers_count = int(input())
points_count = float(input())
season = input()
place = input()
total_sum = 0
if place == 'Bulgaria' and season == 'summer':
    points = dancers_count * points_count
    total_sum = points - (points * 0.05)
elif place == 'Bulgaria' and season == 'winter':
    points = dancers_count * points_count
    total_sum = points - (points * 0.08)
elif place == 'Abroad' and season == 'summer':
    points = dancers_count * points_count
    points_total = points + (points * 0.5)
    total_sum = points_total - (points_total * 0.1)
elif place == 'Abroad' and season == 'winter':
    points = dancers_count * points_count
    points_total = points + (points * 0.5)
    total_sum = points_total - (points_total * 0.15)
money_for_charity = total_sum * 0.75
money_left = total_sum - money_for_charity
money_per_person = money_left / dancers_count
print(f'Charity - {money_for_charity:.2f}')
print(f'Money per dancer - {money_per_person:.2f}')

