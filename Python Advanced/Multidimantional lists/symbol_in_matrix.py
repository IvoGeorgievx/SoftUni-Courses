size = int(input())
matrix = [list(input()) for _ in range(size)]

symbol = input()

found = False

for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == symbol:
            found = True
            print(f'({row_index}, {col_index})')
            break

if not found:
    print(f"{symbol} does not occur in the matrix")
