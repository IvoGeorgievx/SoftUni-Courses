matrix = []

rows, cols = [int(x) for x in input().split()]

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    line = input()

    if line == 'END':
        break

    exploded = line.split(" ")

    if exploded[0] != 'swap' or len(exploded) != 5:
        print('Invalid input!')
        continue
    else:
        row1, col1, row2, col2 = [int(x) for x in exploded[1:]]
        if row1 >= rows or row2 >= rows or col1 >= cols or col2 >= cols or row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0:
            print('Invalid input!')
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

            for row in matrix:
                print(*row, sep=' ')
