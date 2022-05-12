first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(str(number)):
        if (index + 1) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=' ')


