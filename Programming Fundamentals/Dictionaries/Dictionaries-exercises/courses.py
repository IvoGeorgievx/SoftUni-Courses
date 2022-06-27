def courses():
    command = input()
    course = {}

    while command != 'end':
        data = command.split(" : ")
        course_name = data[0]
        student_name = data[1]

        if course_name not in course:
            course[course_name] = []
            course[course_name].append(student_name)
        else:
            course[course_name].append(student_name)

        command = input()

    for key, value in course.items():
        print(f"{key}: {len(value)}")
        for x in range(len(value)):
            print(f"-- {value[x]}")


courses()
