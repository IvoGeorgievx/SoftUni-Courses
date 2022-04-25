count_of_numbers = int(input())
odd_number = 0
even_number = 0

for number in range(1, count_of_numbers + 1):
    current_number = int(input())
    if number % 2 == 0:
        even_number += current_number
    elif number % 2 != 0:
        odd_number += current_number
if even_number == odd_number:
    print('Yes')
    print(f'Sum = {odd_number}')
elif even_number != odd_number:
    print('No')
    print(f'Diff = {abs(odd_number - even_number)}')
