text = input()
sum = 0
for vowel in range(0, len(text)):
    if text[vowel] == 'a':
        sum += 1
    if text[vowel] == 'e':
        sum += 2
    if text[vowel] == 'i':
        sum += 3
    if text[vowel] == 'o':
        sum += 4
    if text[vowel] == 'u':
        sum += 5
print(sum)
