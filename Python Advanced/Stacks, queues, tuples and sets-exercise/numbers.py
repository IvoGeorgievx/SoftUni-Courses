first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

count = int(input())

for _ in range(count):
    command_parts = input().split()
    command = command_parts[0]
    target = command_parts[1]

    if command == 'Add':
        if target == 'First':
            first = first.union([int(x) for x in command_parts[2::]])
        else:
            second = second.union([int(x) for x in command_parts[2::]])
    elif command == 'Remove':
        if target == 'First':
            first = first.difference([int(x) for x in command_parts[2::]])
        else:
            second = second.difference([int(x) for x in command_parts[2::]])

    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
