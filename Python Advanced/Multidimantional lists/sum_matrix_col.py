matrix = []

rows, cols = [int(x) for x in input().split(", ")]


for i in range(rows):
    current_row = [int(x) for x in input().split(" ")]
    matrix.append(current_row)

col_sums = [0] * cols

for row_index in range(rows):
    for col_index in range(cols):
        col_sums[col_index] += matrix[row_index][col_index]

[print(x) for x in col_sums]