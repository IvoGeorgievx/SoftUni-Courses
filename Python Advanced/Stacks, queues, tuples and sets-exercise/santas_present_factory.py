from collections import deque

toys = [int(x) for x in input().split(" ")]
magic = deque([int(x) for x in input().split(" ")])

# presents = {
#     150: 'Doll',
#     250: 'Wooden train',
#     300: 'Teddy bear',
#     400: 'Bicycle',
# }
doll = 0
wooden_train = 0
teddy_bear = 0
bicycle = 0

while toys and magic:
    current_toy = toys.pop()
    current_magic = magic.popleft()
    result = current_magic * current_toy
    if current_toy == 0 or current_magic == 0:
        continue

    if result == 150:
        doll += 1
    elif result == 250:
        wooden_train += 1
    elif result == 300:
        teddy_bear += 1
    elif result == 400:
        bicycle += 1

    if result < 0:
        sum = current_magic + current_toy
        toys.append(sum)

    if result > 0:
        toys.append(current_toy + 15)

    if doll >= 1 and wooden_train >= 1:
        print('yey')
        break
    if bicycle >= 1 and teddy_bear >= 1:
        print('hooraay')
        break

print(doll)
print(wooden_train)
print(bicycle)
print(teddy_bear)