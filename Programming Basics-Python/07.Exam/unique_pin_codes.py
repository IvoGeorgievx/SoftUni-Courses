first_number = int(input())
second_number = int(input())
third_number = int(input())
is_valid = False
for first_num in range(1, first_number + 1):
    if first_num % 2 == 0:
        is_valid = True
        for second_num in range(2, second_number + 1):
            if second_num == 2 or second_num == 3 or second_num == 5 or second_num == 7:
                is_valid = True
                for third_num in range(1, third_number + 1):
                    if third_num % 2 == 0:
                        is_valid = True
                        if is_valid:
                            print(first_num, second_num, third_num)