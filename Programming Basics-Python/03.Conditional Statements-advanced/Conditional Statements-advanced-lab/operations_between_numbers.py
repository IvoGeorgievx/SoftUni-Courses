number_1 = int(input())
number_2 = int(input())
operator = input()

if operator == '+':
    addition = number_1 + number_2
    if addition % 2 == 0:
        print(f'{number_1} + {number_2} = {addition} - even')
    else:
        print(f'{number_1} + {number_2} = {addition} - odd')
elif operator == '-':
    deduction = number_1 - number_2
    if deduction % 2 == 0:
        print(f'{number_1} - {number_2} = {deduction} - even')
    else:
        print(f'{number_1} - {number_2} = {deduction} - odd')
elif operator == '*':
    multiply = number_1 * number_2
    if multiply % 2 == 0:
        print(f'{number_1} * {number_2} = {multiply} - even')
    else:
        print(f'{number_1} * {number_2} = {multiply} - odd')
elif operator == '/':
    if number_2 == 0:
        print(f'Cannot divide {number_1} by zero')
    else:
        print(f'{number_1} / {number_2} = {number_1 / number_2:.2f}')
elif operator == '%' and number_2 != 0:
    module = number_1 % number_2
    print(f'{number_1} % {number_2} = {module}')
else:
    print(f'Cannot divide {number_1} by zero')





