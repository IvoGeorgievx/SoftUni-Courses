def secret_message():
    concealed_mes = input()
    command = input()
    occurrence = 0

    while command != 'Reveal':
        exploded = command.split(":|:")
        current_command = exploded[0]

        if current_command == 'InsertSpace':
            index = int(exploded[1])
            before_the_index = concealed_mes[:index]
            after_index = concealed_mes[index:]
            concealed_mes = before_the_index + ' ' + after_index
            print(concealed_mes)
        elif current_command == 'Reverse' and occurrence == 0:
            occurrence += 1
            substring = exploded[1]
            if substring in concealed_mes:
                concealed_mes = concealed_mes.replace(substring, '')
                substring = substring[::-1]
                concealed_mes = concealed_mes + substring
                print(concealed_mes)
            else:
                print('error')
        elif current_command == 'ChangeAll':
            substring1 = exploded[1]
            replacement = exploded[2]
            concealed_mes = concealed_mes.replace(substring1, replacement)
            print(concealed_mes)
        command = input()

    print(f'You have a new text message: {concealed_mes}')


secret_message()
