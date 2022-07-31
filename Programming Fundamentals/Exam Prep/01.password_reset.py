text = input()

command = input()
new_text = ''
while command != 'Done':
    exploded = command.split(" ")
    action = exploded[0]

    if action == 'TakeOdd':
        for i in range(1, len(text), 2):
            new_text += text[i]
        text = new_text
        print(text)

    elif action == 'Cut':
        index = int(exploded[1])
        length = int(exploded[2])
        text = text[:index] + text[index + length:]
        print(text)

    elif action == 'Substitute':
        substring = exploded[1]
        substituted = exploded[2]
        if substring in text:
            text = text.replace(substring, substituted)
            print(text)
        else:
            print('Nothing to replace!')

    command = input()

print(f'Your password is: {text}')