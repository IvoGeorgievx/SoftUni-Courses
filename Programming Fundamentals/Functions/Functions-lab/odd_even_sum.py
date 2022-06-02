the_num = input()


def odd_and_even_sum():
    odd_sum = 0
    even_sum = 0
    for i in str(the_num):
        if int(i[0]) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


print(odd_and_even_sum())

