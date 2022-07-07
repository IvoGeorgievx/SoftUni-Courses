data = input()

digits = ''
letters = ''
characters = ''

for i in data:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        characters += i

print(digits)
print(letters)
print(characters)
