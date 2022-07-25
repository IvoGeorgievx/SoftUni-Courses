import re

nums = []

while True:

    info = input()

    if not info:
        break

    result = re.findall(r'\d+', info)

    if len(result) > 0:
        print(' '.join(result), end=' ')
