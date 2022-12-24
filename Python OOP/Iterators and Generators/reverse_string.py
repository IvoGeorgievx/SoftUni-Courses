def reverse_text(string):
    index = 0
    n = len(string)

    while index < n:
        yield string[n - index - 1]
        index += 1


for char in reverse_text("step"):
    print(char, end='')
