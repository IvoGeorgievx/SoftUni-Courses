from collections import deque

liters = int(input())
queue = deque()

while True:
    command = input()
    if command == 'Start':
        break
    queue.append(command)


while True:

    other = input()
    if other == 'End':
        break
    elif other.startswith('refill '):
        exploded = other.split(' ')
        liters += int(exploded[1])
    else:
        person = queue.popleft()
        required = int(other)

        if required <= liters:
            print(f'{person} got water')
            liters -= required
        else:
            print(f'{person} must wait')

print(f'{liters} liters left')