import re

info = input()

text = re.finditer(r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))', info)

final_result = []

for match in text:
    final_result.append(match.group())

print(' '.join(final_result))
