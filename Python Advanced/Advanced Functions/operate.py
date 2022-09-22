def operate(operation, *args):
    def add(*args):
        return sum(args)

    def subtract(x, *args):
        return x + sum(-x for x in args)

    def multiply(*args):
        result = 1
        for i in args:
            result *= i
        return result

    def divide(x, *args):
        result = x
        for value in args:
            result /= value
        return result

    if operation == '+':
        return add(*args)
    elif operation == '-':
        return subtract(*args)
    elif operation == '*':
        return multiply(*args)
    else:
        return divide(*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 1, 2, 3))
print(operate("/", 3, 4, 2, 3))
