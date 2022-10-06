from collections import deque

vowels = deque([str(x) for x in input().split()])
consonants = [x for x in input().split()]

words = ['rose', 'tulip', 'lotus', 'daffodil']

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()






