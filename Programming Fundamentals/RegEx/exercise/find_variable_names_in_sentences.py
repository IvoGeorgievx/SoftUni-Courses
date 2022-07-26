import re

pattern = r'\b_[a-zA-Z0-9]+\b'

text = input()

result = re.findall(pattern, text)
final_result = []

for elements in result:
    final_result.append(elements[1:])

print(','.join(final_result))
