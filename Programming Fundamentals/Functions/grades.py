def grade_counter(grade):
    if grade <= 2.99:
        return "Fail"
    elif 3 <= grade <= 3.49:
        return "Poor"
    elif 3.50 <= grade <= 4.49:
        return "Good"
    elif 4.50 <= grade <= 5.49:
        return "Very Good"
    elif grade >= 5.50:
        return "Excellent"


current_grade = float(input())
print(grade_counter(current_grade))

