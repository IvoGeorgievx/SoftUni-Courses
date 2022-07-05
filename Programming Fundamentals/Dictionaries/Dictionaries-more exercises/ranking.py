info = input()
info_dict = {}
user_dict = {}

while info != 'end of contests':
    exploded = info.split(":")
    contest = exploded[0]
    password = exploded[1]

    if contest not in info_dict:
        info_dict[contest] = password

    info = input()

command = input()

while command != 'end of submissions':
    parameters = command.split("=>")
    contest_name = parameters[0]
    password = parameters[1]
    username = parameters[2]
    points = int(parameters[3])

    if contest_name in info_dict:
        if info_dict[contest_name] == password:
            info_dict[contest_name] = {}
            if username not in info_dict:
                info_dict[contest_name][username] = points
            else:
                info_dict[contest_name][username] += points

    command = input()

print(info_dict)