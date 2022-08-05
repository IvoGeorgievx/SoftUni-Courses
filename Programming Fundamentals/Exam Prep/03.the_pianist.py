number_of_piece = int(input())
piece_dict = dict()

for i in range(number_of_piece):
    pieces = input().split("|")
    piece = pieces[0]
    composer = pieces[1]
    key = pieces[2]
    piece_dict[piece] = [composer, key]

command = input()

while command != 'Stop':
    exploded = command.split("|")
    action = exploded[0]

    if action == 'Add':
        piece = exploded[1]
        composer = exploded[2]
        key = exploded[3]
        if piece not in piece_dict:
            piece_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f'{piece} is already in the collection!')

    elif action == 'Remove':
        piece = exploded[1]
        if piece in piece_dict:
            piece_dict.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif action == 'ChangeKey':
        piece = exploded[1]
        new_key = exploded[2]
        if piece in piece_dict:
            piece_dict[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    command = input()

for key, value in piece_dict.items():
    print(f'{key} -> Composer: {value[0]}, Key: {value[1]}')
