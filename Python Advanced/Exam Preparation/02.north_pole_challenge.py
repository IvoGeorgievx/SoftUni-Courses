x, y = [int(x) for x in input().split(', ')]
matrix = []
santa_row = 0
santa_col = 0

for _ in range(x):
    matrix.append(input().split())

for row in range(x):
    for col in range(y):
        if matrix[row][col] == 'Y':
            santa_row = row
            santa_col = col


