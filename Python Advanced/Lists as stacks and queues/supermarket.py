from collections import deque

s = deque()

while True:

    command = input()
    if command == 'End':
        print(f'{len(s)} people remaining')
        break
    elif command == 'Paid':
        while s:
            print(s.popleft())
    else:
        s.append(command)