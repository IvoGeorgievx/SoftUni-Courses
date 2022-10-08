def next_pos(row, col, direction):
    if direction == 'up':
        if rover_row == 0:
            return row + 5, col
        else:
            return row - 1, col

    if direction == 'down':
        if rover_row == 5:
            return row - 5, col
        else:
            return row + 1, col

    if direction == 'left':
        if rover_col == 0:
            return row, col + 5
        else:
            return row, col - 1

    if direction == 'right':
        if rover_col == 5:
            return row, col - 5
        else:
            return row, col + 1


size = 6
matrix = []
rover_row = 0
rover_col = 0
concrete_deposit = 0
metal_deposit = 0
water_deposit = 0


for _ in range(size):
    c_row = input().split(" ")
    matrix.append(c_row)

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'E':
            rover_row = row
            rover_col = col

commands = input().split(", ")
for direction in commands:
    next_row, next_col = next_pos(rover_row, rover_col, direction)

    rover_row, rover_col = next_row, next_col

    if matrix[rover_row][rover_col] == 'C':
        concrete_deposit += 1
        print(f'Concrete deposit found at {(rover_row, rover_col)}')

    elif matrix[rover_row][rover_col] == 'W':
        water_deposit += 1
        print(f'Water deposit found at {(rover_row, rover_col)}')

    elif matrix[rover_row][rover_col] == 'M':
        metal_deposit += 1
        print(f'Metal deposit found at {(rover_row, rover_col)}')

    elif matrix[rover_row][rover_col] == 'R':
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if concrete_deposit > 0 and water_deposit > 0 and metal_deposit > 0:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')





