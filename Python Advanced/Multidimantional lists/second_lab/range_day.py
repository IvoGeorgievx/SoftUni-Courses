def is_move_valid(my_pos_row, my_pos_col, direction, moves):
    if direction == 'up':
        return my_pos_row - moves, my_pos_col
    if direction == 'down':
        return my_pos_row + moves, my_pos_col
    if direction == 'left':
        return my_pos_row, my_pos_col - moves
    if direction == 'right':
        return my_pos_row, my_pos_col + moves


def is_inside(next_row, next_col, matrix):
    return 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix)


size = 5
matrix = []
my_pos_row = 0
my_pos_col = 0
targets = 0
hit_targets = []

for _ in range(5):
    matrix.append(input().split(" "))

for row in range(5):
    for col in range(5):
        if matrix[row][col] == 'A':
            my_pos_row = row
            my_pos_col = col
        elif matrix[row][col] == 'x':
            targets += 1

matrix[my_pos_row][my_pos_col] = '.'

command_count = int(input())

for _ in range(command_count):
    current_command = input().split()
    direction = current_command[1]

    if current_command[0] == 'move':
        moves = int(current_command[2])
        next_row, next_col = is_move_valid(my_pos_row, my_pos_col, direction, moves)
        if is_inside(next_row, next_col, matrix) and matrix[next_row][next_col] == '.':
            my_pos_row, my_pos_col = next_row, next_col

    else:
        shoot_row, shoot_col = is_move_valid(my_pos_row, my_pos_col, direction, 1)
        while is_inside(shoot_row, shoot_col, matrix):
            if matrix[shoot_row][shoot_col] == 'x':
                targets -= 1
                matrix[shoot_row][shoot_col] = '.'
                hit_targets.append([shoot_row, shoot_col])
                break
            shoot_row, shoot_col = is_move_valid(shoot_row, shoot_col, direction, 1)
        if targets == 0:
            break

if targets == 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

print(*hit_targets, sep='\n')



