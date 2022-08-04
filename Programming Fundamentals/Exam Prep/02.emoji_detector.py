import re


info = input()
res = 1
for i in info:
    if i.isdigit():
        res *= int(i)

pattern = r'([\:\:|\*\*]){2}([A-Z][a-z]{2,})\1{2}'

total_group = []
cool_group = []

result = re.finditer(pattern, info)
print(f'Cool threshold: {res}')
for r in result:
    sum(ord(ch) for ch in r.group(2))
    total_group.append(r.group(2))
    if sum(ord(ch) for ch in r.group(2)) > res:
        cool_group.append(r.group())
print(f"{len(total_group)} emojis found in the text. The cool ones are:")
for element in cool_group:
    print(element)


