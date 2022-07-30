def imitation_game():
    encrypted_text = input()

    while True:

        command = input()

        if command == 'Decode':
            break

        exploded = command.split('|')
        instruction = exploded[0]

        if instruction == 'Move':
            number_of_letters = int(exploded[1])
            before = encrypted_text[:number_of_letters]
            after = encrypted_text[number_of_letters:]
            encrypted_text = after + before

        elif instruction == 'Insert':
            index = int(exploded[1])
            value = exploded[2]
            before = encrypted_text[:index]
            after = encrypted_text[index:]
            encrypted_text = before + value + after

        elif instruction == 'ChangeAll':
            substring = exploded[1]
            replacement = exploded[2]
            encrypted_text = encrypted_text.replace(substring, replacement)

    print(f'The decrypted message is: {encrypted_text}')


imitation_game()
