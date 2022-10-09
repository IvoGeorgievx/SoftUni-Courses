def white_moves(white_row, white_col):
    return white_row - 1, white_col


def black_moves(black_row, black_col, board):
    return black_row + 1, black_col


def is_pawn_around_white(white_row, white_col, board, winner_coords):
    if 0 <= white_col - 1 and white_col + 1 < len(board):
        if board[white_row - 1][white_col + 1] != '-':
            winner_coords = board_final[white_row - 1][white_col + 1]
        elif board[white_row - 1][white_col - 1] != '-':
            winner_coords = board_final[white_row - 1][white_col - 1]
    return winner_coords


def is_pawn_around_black(black_row, black_col, board, winner_coords):
    if 0 <= black_col - 1 and black_col + 1 < len(board):
        if board[black_row + 1][black_col + 1] != '-':
            winner_coords = board_final[black_row + 1][black_col + 1]
        if board[black_row + 1][black_col - 1] != '-':
            winner_coords = board_final[black_row + 1][black_col - 1]
    return winner_coords


board_final = [

    ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
    ['a7', 'b7', 'c7', 'd7', 'e7', '71', 'g7', 'h7'],
    ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
    ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
    ['a4', 'b4', 'c4', 'd4', 'e4', '41', 'g4', 'h4'],
    ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
    ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
    ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],

]

size = 8
board = []
white_row = 0
white_col = 0
black_row = 0
black_col = 0
total_turns = 0
board_final_row = 0
board_final_col = 0

for _ in range(size):
    board.append(input().split(" "))

for row in range(size):
    for col in range(size):

        if board[row][col] == 'w':
            white_row = row
            white_col = col

        elif board[row][col] == 'b':
            black_row = row
            black_col = col

turns = ['White', 'Black']

while True:
    current_turn = turns[0]
    winner_coords = 0

    if current_turn == 'White':
        if is_pawn_around_white(white_row, white_col, board, winner_coords):
            print(f"Game over! {current_turn} win, capture on {winner_coords}.")
            break

        next_w_row, next_w_col = white_moves(white_row, white_col)
        if next_w_row < 0:
            print(f'Game over! {current_turn} pawn is promoted to a queen at {board_final[white_row][white_col]}.')
            break
        else:
            white_row, white_col = next_w_row, next_w_col
            board[white_row][white_col] = 'w'
    else:
        if is_pawn_around_black(black_row, black_col, board, board_final):
            print(f"Game over! {current_turn} win, capture on .")
            break

        next_b_row, next_b_col = black_moves(black_row, black_col, board)
        if next_b_row == len(board):
            print(f'Game over! {current_turn} pawn is promoted to a queen at {board_final[black_row][black_col]}.')
            break
        else:
            black_row, black_col = next_b_row, next_b_col
            board[black_row][black_col] = 'b'

    turns[0], turns[1] = turns[1], turns[0]
