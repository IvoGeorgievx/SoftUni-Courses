event = input().split('|')
energy = 100
coins = 100
condition = False

for i in event:
    current_event = i.split("-")
    event_type = current_event[0]
    event_value = int(current_event[1])
    if event_type == 'rest':
        energy += event_value
        if energy > 100:
            energy = 100
            print('You gained 0 energy.')
            print(f'Current energy: {energy}.')
        else:
            print(f'You gained {event_value} energy.')
            print(f'Current energy: {energy}.')
    elif event_type == 'order':
        if energy >= 30:
            coins += event_value
            energy -= 30
            print(f'You earned {event_value} coins.')
        else:
            energy += 50
            print('You had to rest!')
    elif event_type != 'order' and event_type != 'rest':
        if coins >= event_value:
            print(f'You bought {event_type}.')
            coins -= event_value

        else:
            print(f'Closed! Cannot afford {event_type}.')
            condition = True
            break
if not condition:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
