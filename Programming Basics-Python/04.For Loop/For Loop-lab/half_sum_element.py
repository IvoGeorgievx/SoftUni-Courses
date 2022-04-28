import sys
numbers_count = int(input())
highest_number = -sys.maxsize
other_numbers_sum = 0

for i in range(0, numbers_count):
    numbers = int(input())
    other_numbers_sum += numbers

    if numbers > highest_number:
        highest_number = numbers
other_numbers_sum = other_numbers_sum - highest_number
if highest_number == other_numbers_sum:
    print('Yes')
    print(f'Sum = {highest_number}')
else:
    print('No')
    print(f'Diff = {abs(other_numbers_sum - highest_number)}')
