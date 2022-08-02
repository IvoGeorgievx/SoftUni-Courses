def world_tour():
    destinations = input()
    command = input()

    while command != 'Travel':
        exploded = command.split(":")
        current_command = exploded[0]

        if current_command == 'Add Stop':
            index = int(exploded[1])
            new_string = exploded[2]
            if 0 <= index <= len(destinations):
                destinations = destinations[:index] + new_string + destinations[index:]
        elif current_command == 'Remove Stop':
            start_index = int(exploded[1])
            end_index = int(exploded[2])
            if 0 <= start_index <= end_index < len(destinations):
                destinations = destinations[:start_index] + destinations[end_index + 1:]
        elif current_command == 'Switch':
            old_string = exploded[1]
            new_string1 = exploded[2]
            if old_string in destinations:
                destinations = destinations.replace(old_string, new_string1)
        print(destinations)

        command = input()
    print(f"Ready for world tour! Planned stops: {destinations}")


world_tour()
