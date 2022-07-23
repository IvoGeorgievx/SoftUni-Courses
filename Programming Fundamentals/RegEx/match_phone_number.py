import re

info = input()

text = re.finditer(r'\+359([ -])2\1\d{3}\1\d{4}\b', info)

final_result = []

for match in text:
    final_result.append(match.group())

print(', '.join(final_result))
