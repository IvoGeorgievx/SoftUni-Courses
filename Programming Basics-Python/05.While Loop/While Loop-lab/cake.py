w = int(input())
l = int(input())

cake_pieces = w * l

while True:
    piece = input()
    if piece == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        break

    cake_pieces -= int(piece)

    if cake_pieces <= 0:
        print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
        break


