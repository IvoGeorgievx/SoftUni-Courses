cars_count = int(input())

ss = set()

for i in range(cars_count):
    command = input().split(", ")
    if command[0] == 'IN':
        ss.add(command[1])
    elif command[0] == 'OUT':
        ss.remove(command[1])

if len(ss) > 0:
    for i in ss:
        print(i)
else:
    print('Parking Lot is Empty')
