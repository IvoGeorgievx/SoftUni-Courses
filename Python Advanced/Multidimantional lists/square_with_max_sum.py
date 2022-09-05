matrix = []

rows, cols = [int(x) for x in input().split(", ")]

for _ in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix.append(current_row)

best_sum = float('-inf')
best_row = 0
best_col = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_sum = matrix[row_index][col_index] + matrix[row_index + 1][col_index] \
                      + matrix[row_index][col_index + 1] + matrix[row_index + 1][col_index + 1]

        if current_sum > best_sum:
            best_sum = current_sum
            best_row = row_index
            best_col = col_index

print(f'{matrix[best_row][best_col]} {matrix[best_row][best_col + 1]}')
print(f'{matrix[best_row + 1][best_col]} {matrix[best_row + 1][best_col + 1]}')
print(best_sum)