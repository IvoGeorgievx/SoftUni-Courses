def print_func(students_dict):
    print(f"Results:")


def softuni_exam_results():
    command = input()
    students_dict = {}

    while True:

        if command == 'exam finished':
            print_func(students_dict)
            break

        if 'banned' not in command:
            data = command.split("-")
            username = data[0]
            language = data[1]
            points = data[2]

            if username not in students_dict:
                students_dict[username] = {}
                students_dict[username][language] = points
                if students_dict[username][language] < points:
                    students_dict[username][language] = points

        else:
            data = command.split("-")
            username = data[0]

            if username in students_dict.keys():
                students_dict.pop(username)

        command = input()


softuni_exam_results()
