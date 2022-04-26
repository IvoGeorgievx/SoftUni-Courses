count_of_numbers = int(input())
left_side = 0
right_side = 0

for numbers in range(2 * count_of_numbers):
    current_number = int(input())
    if numbers < count_of_numbers:
        left_side += current_number
    else:
        right_side += current_number
if left_side == right_side:
    print(f'Yes, sum = {right_side}')
else:
    print(f'No, diff = {abs(left_side - right_side)}')
