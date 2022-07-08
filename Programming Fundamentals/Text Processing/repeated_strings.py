data = input().split()
result = ''

for word in data:
    length = len(word)
    result += length * word

print(result)