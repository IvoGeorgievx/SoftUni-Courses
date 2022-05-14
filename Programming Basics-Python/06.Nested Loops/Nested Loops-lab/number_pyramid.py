number = int(input())
current = 0
current_equal_to_num = False
for rows in range(1, number + 1):
    for columns in range(1, rows + 1):
        current += 1
        print(current, end=' ')
        if current == number:
            current_equal_to_num = True
            break
    if current_equal_to_num:
        break
    print()



