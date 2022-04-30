number = int(input())
total_score = 0
number_count = 0
from_zero_to_nine = 0
from_ten_to_nineteen = 0
from_twenty_to_tnine = 0
from_thirty_to_tnine = 0
from_forty_to_fifty = 0
invalid_numbers = 0
for _ in range(number):
    num = int(input())
    if 0 <= num <= 9:
        total_score += num * 0.2
        from_zero_to_nine += 1
    elif 10 <= num <= 19:
        total_score += num * 0.3
        from_ten_to_nineteen += 1
    elif 20 <= num <= 29:
        total_score += num * 0.4
        from_twenty_to_tnine += 1
    elif 30 <= num <= 39:
        total_score += 50
        from_thirty_to_tnine += 1
    elif 40 <= num <= 50:
        total_score += 100
        from_forty_to_fifty += 1
    elif num < 0 or num > 50:
        total_score /= 2
        invalid_numbers += 1
    number_count += 1
print(f'{total_score:.2f}')
print(f'From 0 to 9: {from_zero_to_nine / number * 100:.2f}%')
print(f'From 10 to 19: {from_ten_to_nineteen / number * 100:.2f}%')
print(f'From 20 to 29: {from_twenty_to_tnine / number * 100:.2f}%')
print(f'From 30 to 39: {from_thirty_to_tnine / number * 100:.2f}%')
print(f'From 40 to 50: {from_forty_to_fifty / number * 100:.2f}%')
print(f'Invalid numbers: {invalid_numbers / number * 100:.2f}%')