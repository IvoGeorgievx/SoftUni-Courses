activation_key = input()

command = input()

while command != 'Generate':
    exploded = command.split(">>>")
    action = exploded[0]

    if action == 'Contains':
        substring = exploded[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == 'Flip':
        upp_or_low = exploded[1]
        start_index = int(exploded[2])
        end_index = int(exploded[3])
        if upp_or_low == 'Upper':
            upper_part = activation_key[start_index:end_index]
            upper_part = upper_part.upper()
            activation_key = activation_key[:start_index] + upper_part + activation_key[end_index:]
            print(activation_key)

        elif upp_or_low == 'Lower':
            lower_part = activation_key[start_index:end_index]
            lower_part = lower_part.lower()
            activation_key = activation_key[:start_index] + lower_part + activation_key[end_index:]
            print(activation_key)

    elif action == 'Slice':
        start_index = int(exploded[1])
        end_index = int(exploded[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]

        print(activation_key)

    command = input()

print(f'Your activation key is: {activation_key}')