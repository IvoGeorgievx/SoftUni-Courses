judge_count = int(input())
assessment_name = input()
average_grade_total = 0
presentation_count = 0
while assessment_name != 'Finish':
    average_score = 0
    for _ in range(judge_count):
        assessment_grade = float(input())
        average_score += assessment_grade
    average_score /= judge_count
    print(f'{assessment_name} - {average_score:.2f}.')
    average_grade_total += average_score
    presentation_count += 1

    assessment_name = input()

average_grade_total /= presentation_count
print(f"Student's final assessment is {average_grade_total:.2f}.")


