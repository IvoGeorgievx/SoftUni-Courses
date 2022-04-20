junior_cyclists = int(input())
senior_cyclists = int(input())
track_type = input()

juniors = 0
seniors = 0
total_cyclists = junior_cyclists + senior_cyclists
if track_type == 'trail':
    juniors = 5.50
    seniors = 7
elif track_type == 'cross-country':
    juniors = 8
    seniors = 9.50
    if total_cyclists >= 50:
        juniors = juniors - (juniors * 0.25)
        seniors = seniors - (seniors * 0.25)
elif track_type == 'downhill':
    juniors = 12.25
    seniors = 13.75
elif track_type == 'road':
    juniors = 20
    seniors = 21.50
total_income = (junior_cyclists * juniors) + (senior_cyclists * seniors)
discount = total_income - (total_income * 0.05)
print(f'{discount:.2f}')


