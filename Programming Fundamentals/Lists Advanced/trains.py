number_of_wagons = int(input())
train = [0 for i in range(number_of_wagons)]

command = input()

while command != 'End':
    splitted_command = command.split(" ")
    current_command = splitted_command[0]
    if current_command == 'add':
        num_people = int(splitted_command[1])
        train[-1] += num_people
    if current_command == 'insert':
        position = int(splitted_command[1])
        num_people = int(splitted_command[2])
        train[position] += num_people
    if current_command == 'leave':
        position = int(splitted_command[1])
        num_people = int(splitted_command[2])
        train[position] -= num_people

    command = input()

print(train)
