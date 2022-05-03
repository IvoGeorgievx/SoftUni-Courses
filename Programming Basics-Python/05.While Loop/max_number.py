import sys
from sys import maxsize

biggest_number = -sys.maxsize
number = input()

while number != 'Stop':
    current_number = int(number)
    if current_number > biggest_number:
        biggest_number = current_number
    number = input()
print(biggest_number)




