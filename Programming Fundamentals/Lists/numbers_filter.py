numbers_count = int(input())
even = list()
odd = list()
positive = list()
negative = list()

for _ in range(numbers_count):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    if number % 2 != 0:
        odd.append(number)
    if number < 0:
        negative.append(number)
    if number >= 0:
        positive.append(number)
command = input()

print(eval(command))