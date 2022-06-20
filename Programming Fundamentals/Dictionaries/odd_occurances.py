words = input().split(" ")
words = list(map(lambda w: w.lower(), words))
occurrances = {}

for word in words:
    if word not in occurrances:
        occurrances[word] = 1
    else:
        occurrances[word] += 1

odd_words = []

for word in occurrances.keys():
    if occurrances[word] % 2 != 0:
        odd_words.append(word)

print(' '.join(odd_words))
