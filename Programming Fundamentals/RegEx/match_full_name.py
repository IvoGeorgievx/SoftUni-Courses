import re

info = input()

text = re.findall(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b', info)

print(' '.join(text))