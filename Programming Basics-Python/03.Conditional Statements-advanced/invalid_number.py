# Дадено число е валидно, ако е в диапазона [100…200] или е 0.
# Да се напише програма, която чете цяло число
# , въведено от потребителя, и печата "invalid" ако въведеното число не е валидно.
number = int(input())
invalid_or_valid = ''

if 100 <= number <= 200 or number == 0:
    invalid_or_valid = ''
else:
    invalid_or_valid = 'invalid'
print(invalid_or_valid)
