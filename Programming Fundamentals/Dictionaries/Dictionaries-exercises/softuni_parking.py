def parking():

    registrations = dict()
    number_of_commands = int(input())

    for i in range(number_of_commands):
        command = input()

        data = command.split(" ")
        username = data[1]

        if data[0] == 'register':
            plate_number = data[2]
            if username not in registrations:
                registrations[username] = [plate_number]
                print(f"{username} registered {plate_number} successfully")
            else:
                print(f"ERROR: already registered with plate number {plate_number}")
        elif data[0] == 'unregister':
            if username not in registrations:
                print(f"ERROR: user {username} not found")
            else:
                del registrations[username]
                print(f"{username} unregistered successfully")

    for key, value in registrations.items():
        print(f"{key} => {', '.join(value)}")


parking()