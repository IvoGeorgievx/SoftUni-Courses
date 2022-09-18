def next_move(santa_row, santa_col, direction):
    if direction == 'up':
        return santa_row - 1, santa_col
    if direction == 'down':
        return santa_row + 1, santa_col
    if direction == 'left':
        return santa_row, santa_col - 1
    if direction == 'right':
        return santa_row, santa_col + 1


def is_inside(next_row, next_col, matrix):
    return 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix)

count_of_presents = int(input())
size = int(input())
matrix = []
santa_row = 0
santa_col = 0
happy_kids = 0
happy_kids_count = 0
kids = [

]

for _ in range(size):
    matrix.append(input().split())

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'S':
            santa_row = row
            santa_col = col
        elif matrix[row][col] == 'V':
            happy_kids_count += 1

matrix[santa_row][santa_col] = '-'

while True:
    command = input()

    if command == 'Christmas morning' or count_of_presents == 0:
        break

    next_row, next_cal = next_move(santa_row, santa_col, command)
    if is_inside(next_row, next_cal, matrix):
        santa_row, santa_col = next_row, next_cal

        if matrix[santa_row][santa_col] == 'X':
            kids.append([santa_row, santa_col])
            matrix[santa_row][santa_col] = '-'

        elif matrix[santa_row][santa_col] == 'C':
            happy_kids += are_kids_around(santa_row, santa_col, matrix)
            count_of_presents -= are_kids_around(santa_row, santa_col, matrix)

        elif matrix[santa_row][santa_col] == 'V':
            kids.append([santa_row, santa_col])
            happy_kids += 1
            happy_kids_count -= 1
            count_of_presents -= 1
            matrix[santa_row][santa_col] = '-'
        else:
            continue
    else:
        continue

    if count_of_presents <= 0 and happy_kids_count > 0:
        print("Santa ran out of presents!")
        break

for row in matrix:
    print(*row, sep=" ")

if happy_kids > 0:
    print(f"Good job, Santa! {happy_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {happy_kids_count} nice kid/s.")








