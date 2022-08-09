initial = input()
ending = []

for ch in initial:
    ending.append(ch)

reversed_string = ''

while ending:
    reversed_string += ending.pop()

print(reversed_string)