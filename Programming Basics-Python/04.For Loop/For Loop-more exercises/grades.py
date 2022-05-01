students_count = int(input())
student_grade = 0

top_students = 0
between_4_and_5 = 0
between_3_and_4 = 0
failed_students = 0
students_grade_total = 0

top_student_percentage = 0
between_3_and_4_percentage = 0
between_4_and_5_percentage = 0
failed_percentage = 0
average = 0

for n in range(1, students_count + 1):
    student_grade = float(input())
    if 2 <= student_grade <= 2.99:
        students_grade_total += student_grade
        failed_students += 1
    elif 3 <= student_grade <= 3.99:
        students_grade_total += student_grade
        between_3_and_4 += 1
    elif 4 <= student_grade <= 4.99:
        students_grade_total += student_grade
        between_4_and_5 += 1
    elif student_grade >= 5.00:
        students_grade_total += student_grade
        top_students += 1
    top_student_percentage = top_students / students_count * 100
    between_4_and_5_percentage = between_4_and_5 / students_count * 100
    between_3_and_4_percentage = between_3_and_4 / students_count * 100
    failed_percentage = failed_students / students_count * 100
    average = students_grade_total / students_count

print(f'Top students: {top_student_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {between_4_and_5_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {between_3_and_4_percentage:.2f}%')
print(f'Fail: {failed_percentage:.2f}%')
print(f'Average: {average:.2f}')



