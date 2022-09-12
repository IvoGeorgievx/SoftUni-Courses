def next_step(miner_pos_row, miner_pos_col, current_command):
    if current_command == 'up':
        return miner_pos_row - 1, miner_pos_col
    if current_command == 'down':
        return miner_pos_row + 1, miner_pos_col
    if current_command == 'left':
        return miner_pos_row, miner_pos_col - 1
    if current_command == 'right':
        return miner_pos_row, miner_pos_col + 1


def is_inside(next_row, next_col, matrix):
    return 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix)


size = int(input())
commands = input().split()

matrix = []
miner_pos_row = 0
miner_pos_col = 0
coals = 0
game_over = False

for _ in range(size):
    matrix.append(input().split())

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 's':
            miner_pos_row = row
            miner_pos_col = col
        elif matrix[row][col] == 'c':
            coals += 1

for current_command in commands:
    next_row, next_col = next_step(miner_pos_row, miner_pos_col, current_command)

    if is_inside(next_col, next_row, matrix):
        miner_pos_row, miner_pos_col = next_row, next_col

    else:
        continue

    if matrix[miner_pos_row][miner_pos_col] == 'e':
        game_over = True
        print(f'Game over! ({miner_pos_row}, {miner_pos_col})')
    elif matrix[miner_pos_row][miner_pos_col] == 'c':
        coals -= 1
        matrix[miner_pos_row][miner_pos_col] = '*'

    if coals == 0:
        print(f"You collected all coal! ({miner_pos_row}, {miner_pos_col})")
        break
if coals > 0 and not game_over:
    print(f"{coals} pieces of coal left. ({miner_pos_row}, {miner_pos_col})")