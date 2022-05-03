student_name = input()
current_class = 1
bad_grade_counter = 0
expelled = False
grade = 0

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_grade_counter += 1
        if bad_grade_counter == 2:
            expelled = True
            break
        continue
    grade += current_grade
    current_class += 1
if expelled:
    print(f'{student_name} has been excluded at {current_class} grade')
else:
    average_grade = grade / 12
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
