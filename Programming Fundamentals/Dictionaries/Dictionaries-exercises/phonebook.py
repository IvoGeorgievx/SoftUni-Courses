def phone_book_information(number_of_lines, phone_book):
    for x in range(number_of_lines):
        name = input()
        if name not in phone_book:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phone_book[name]}")
    return True


def phone_book_info():
    phone_book = {}
    condition = False

    while True:

        data = input().split("-")

        if data[0].isdigit():
            condition = phone_book_information(int(data[0]), phone_book)
        else:
            phone_book[data[0]] = data[1]

        if condition:
            break


phone_book_info()