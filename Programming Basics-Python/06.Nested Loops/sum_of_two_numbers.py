start = int(input())
final = int(input())
magic_number = int(input())
combination_count = 0
combination = False
for first_number in range(start, final + 1):
    for second_number in range(start, final + 1):
        combination_count += 1
        if first_number + second_number == magic_number:
            combination = True
            break
    if combination:
        break
if combination:
    print(f'Combination N:{combination_count} ({first_number} + {second_number} = {magic_number})')
else:
    print(f'{combination_count} combinations - neither equals {magic_number}')


