days_to_stay = int(input())
type_of_room = input()
assessment = input()
nights_to_stay = days_to_stay - 1
room = 0

if type_of_room == 'room for one person':
    room = 18
elif type_of_room == 'apartment':
    room = 25
    if nights_to_stay < 10:
        room = room - (room * 0.3)
    elif 10 <= nights_to_stay <= 15:
        room = room - (room * 0.35)
    elif nights_to_stay > 15:
        room = room - (room * 0.5)
elif type_of_room == 'president apartment':
    room = 35
    if nights_to_stay < 10:
        room = room - (room * 0.1)
    elif 10 <= nights_to_stay <= 15:
        room = room - (room * 0.15)
    elif nights_to_stay > 15:
        room = room - (room * 0.2)
total_cost = nights_to_stay * room
if assessment == 'positive':
    total_cost = total_cost + (total_cost * 0.25)
elif assessment == 'negative':
    total_cost = total_cost - (total_cost * 0.1)
print(f'{total_cost:.2f}')




