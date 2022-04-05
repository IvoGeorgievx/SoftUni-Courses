from math import floor

required_hours = int(input())
days_to_go = int(input())
overtime_workers = int(input())

employee_training = days_to_go - (days_to_go * 0.1)
working_hours_left = employee_training * 8
overtime = days_to_go * overtime_workers * 2
total_hours = working_hours_left + overtime
if total_hours >= required_hours:
    print(f'Yes!{floor(total_hours - required_hours)} hours left.')
else:
    print(f'Not enough time!{abs(floor(total_hours - required_hours))} hours needed.')

