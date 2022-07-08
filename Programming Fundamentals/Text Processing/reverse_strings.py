strings = input()

while strings != 'end':
    new_string = strings[::-1]
    print(f"{strings} = {new_string}")

    strings = input()