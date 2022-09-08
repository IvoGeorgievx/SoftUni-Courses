size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])

main_sum = []
secondary_sum = []

for index in range(size):
    main_sum.append(matrix[index][index])
    secondary_sum.append(matrix[index][size - 1 - index])

print(f'Primary diagonal: {", ".join([str(x) for x in main_sum])}. Sum: {sum(main_sum)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_sum])}. Sum: {sum(secondary_sum)}')
