import re

info = input()

text = re.finditer(r'(\b\d{2})([/.-])([A-Z][a-z]{2})\2(\d{4})', info)

final_result = []

for match in text:
    print(f"Day: {match[1]}, Month: {match[3]}, Year: {match[4]}")
