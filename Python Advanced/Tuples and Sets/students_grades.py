number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    current_student = input().split()
    student, grade = [x for x in current_student]
    if student not in students:
        students[student] = [float(grade)]
    else:
        students[student] += [float(grade)]

for key, value in students.items():
    avg = sum(value) / len(value)
    print(f'{key} -> {value}')


