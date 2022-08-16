expression = input().split(" ")
dd = {}

for x in expression:
    if x not in dd:
        dd[x] = 1
    else:
        dd[x] += 1

for key, value in dd.items():
    print(f'{float(key):.1f} - {value} times')