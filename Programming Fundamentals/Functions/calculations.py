def calculator(operator, a, b):
    if operator == 'multiply':
        return int(a * b)
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'subtract':
        return int(a - b)
    else:
        return int(a + b)


current_operator = input()
current_a = int(input())
current_b = int(input())
print(calculator(current_operator, current_a, current_b))
