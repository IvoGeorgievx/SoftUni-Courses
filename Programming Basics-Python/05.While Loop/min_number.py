import sys
from sys import maxsize
min_number = sys.maxsize
number = input()

while number != 'Stop':
    current_number = int(number)
    if current_number < min_number:
        min_number = current_number
    number = input()
print(min_number)