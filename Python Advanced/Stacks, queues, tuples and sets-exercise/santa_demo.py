from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

presents = {
    150: 0,
    250: 0,
    300: 0,
    400: 0,
}
while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    result = current_material * current_magic

    if current_material == 0 or current_magic == 0:
        continue

    elif result < 0:
        materials.append(result)

    elif result not in presents and result > 0:
        materials.append(current_material + 15)

    elif result in presents:
        presents[result] += 1

print(presents)



