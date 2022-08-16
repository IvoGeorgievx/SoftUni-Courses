from collections import deque

toys = [int(x) for x in input().split(" ")]
magic = deque([int(x) for x in input().split(" ")])

# presents = {
#     150: 'Doll',
#     250: 'Wooden train',
#     300: 'Teddy bear',
#     400: 'Bicycle',
# }

toys_total = {}

doll = 0
wooden_train = 0
teddy_bear = 0
bicycle = 0

while toys and magic:
    current_toy = toys.pop()
    current_magic = magic.popleft()
    result = current_magic * current_toy
    if current_toy == 0:
        magic.appendleft(current_magic)
        continue
    if current_magic == 0:
        toys.append(current_toy)
    if current_magic == 0 and current_toy == 0:
        continue
    if result == 150:
        doll += 1
    elif result == 250:
        wooden_train += 1
    elif result == 300:
        teddy_bear += 1
    elif result == 400:
        bicycle += 1
    else:
        if result > 0:
            toys.append(current_toy + 15)

    if result < 0:
        sum = current_magic + current_toy
        toys.append(sum)

if doll >= 1 and wooden_train >= 1 or bicycle >= 1 and teddy_bear >= 1:
    print('The presents are crafted! Merry Christmas!')
else:
    print("No presents this Christmas!")

if toys:
    print(f'{", ".join(sorted([str(x) for x in toys]))}')

if magic:
    print(f'{", ".join(sorted([str(x) for x in magic]))}')

if doll:
    print(f'{doll}')