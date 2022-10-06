from collections import deque

elves = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

toys_created = 0
turns = 0
energy = 0

while elves and materials:
    current_elf = elves.popleft()
    current_material = materials.pop()
    turns += 1

    if turns % 3 != 0 and turns % 5 != 0:

        if current_elf >= current_material:
            current_elf -= current_material
            toys_created += 1
            energy += current_material
            elves.append(current_elf + 1)
        else:
            materials.append(current_material)
            elves.append(current_elf * 2)

    elif turns % 3 == 0:
        current_material = current_material * 2
        if current_elf >= current_material:
            current_elf -= current_material
            energy += current_material
            toys_created += 2
            elves.append(current_elf + 1)
        else:
            materials.append(int(current_material / 2))
            elves.append(current_elf * 2)

    elif turns % 5 == 0:
        if current_elf >= current_material:
            current_elf -= current_material
            energy += current_material
            elves.append(current_elf)
        else:
            materials.append(current_material)
            elves.append(current_elf * 2)

print(toys_created)
print(energy)
print(elves)
print(materials)






