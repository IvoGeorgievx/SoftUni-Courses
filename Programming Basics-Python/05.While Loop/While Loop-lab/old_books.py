desired_book = input()
book_counter = 0

while desired_book != 'No More Books':
    new_book = input()
    if new_book == desired_book:
        print(f'You checked {book_counter} books and found it.')
        break
    if new_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break
    book_counter += 1

