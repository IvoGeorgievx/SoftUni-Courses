first_char = input()
second_char = input()


def ascii_return(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=' ')


ascii_return(first_char, second_char)
