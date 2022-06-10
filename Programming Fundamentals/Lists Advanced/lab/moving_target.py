target_sequence = list(map(int, input().split(" ")))
command = input()

while command != "End":
    exploded = command.split(" ")
    index = int(exploded[1])
    if exploded[0] == 'Shoot':
        power = int(exploded[2])
        if index in range(len(target_sequence)):
            target_sequence[index] -= power
            if target_sequence[index] <= 0:
                target_sequence.pop(index)
    elif exploded[0] == 'Add':
        value = int(exploded[2])
        if index in range(len(target_sequence)):
            target_sequence.insert(index, value)
        else:
            print("Invalid placement!")
    elif exploded[0] == 'Strike':
        radius = int(exploded[2])
        if index in range(len(target_sequence)) and (index + radius) in range(len(target_sequence)) \
                and (index - radius) in range(len(target_sequence)):
            del target_sequence[(index - radius):(index + radius + 1)]
        else:
            print("Strike missed!")

    command = input()

target_sequence_final = [str(a) for a in target_sequence]
print('|'.join(target_sequence_final))
