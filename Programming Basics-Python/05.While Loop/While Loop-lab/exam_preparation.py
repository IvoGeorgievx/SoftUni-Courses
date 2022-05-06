bad_grades = int(input())
bad_grade_counter = 0
passed = True
score = 0
assignments_count = 0
last_assignment = ''
assignment_name = input()

while assignment_name != 'Enough':
    assignment_grade = int(input())
    last_assignment = assignment_name

    if assignment_grade <= 4:
        bad_grade_counter += 1
        if bad_grade_counter == bad_grades:
            print(f'You need a break, {bad_grade_counter} poor grades.')
            passed = False
            break
    assignment_name = input()
    assignments_count += 1
    score += assignment_grade

if passed:
    average_score = score / assignments_count
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {assignments_count}')
    print(f'Last problem: {last_assignment}')
