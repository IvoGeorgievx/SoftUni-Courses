command = input()
saved = 0
while command != 'End':
    destination = command
    budget = float(input())
    saved = 0
    while budget > saved:
        save = float(input())
        saved += save
    print(f'Going to {destination}!')
    command = input()