first_num = int(input())
second_num = int(input())
third_num = int(input())


def sum_nums():
    return first_num + second_num


def subtract():
    return (sum_nums() - third_num)


def add_and_subtract():
    return subtract()


print(add_and_subtract())