matrix = []

size = int(input())

for _ in range(size):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

diagonal_sum = 0

for col_index in range(size):
    for row_index in range(size):
        if col_index == row_index:
            diagonal_sum += matrix[col_index][row_index]

print(diagonal_sum)