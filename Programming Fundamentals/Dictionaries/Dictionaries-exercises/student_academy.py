def student_academy():
    count = int(input())
    students = {}

    for i in range(count):
        student_name = input()
        student_grade = float(input())

        if student_name not in students:
            students[student_name] = []
            students[student_name].append(student_grade)
        else:
            students[student_name].append(student_grade)

    for key, value in students.items():
        if sum(value) / len(value) >= 4.50:
            print(f"{key} -> {sum(value) / len(value):.2f}")


student_academy()
