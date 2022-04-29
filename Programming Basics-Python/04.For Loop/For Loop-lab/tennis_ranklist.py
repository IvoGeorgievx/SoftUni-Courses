from math import floor
tournaments = int(input())
starting_points = int(input())
# place_taken_points = input()
winner = 0
points_earned = 0
w = 2000
f = 1200
sf = 720

for i in range(tournaments):
    finish_points = input()
    if finish_points == 'W':
        points_earned += w
        winner += 1
    elif finish_points == 'F':
        points_earned += f
    elif finish_points == 'SF':
        points_earned += sf
total_points_earned = points_earned + starting_points
average_points = points_earned / tournaments
win_percent = winner / tournaments * 100
print(f'Final points: {total_points_earned}')
print(f'Average points: {floor(average_points)}')
print(f'{win_percent:.2f}%')







