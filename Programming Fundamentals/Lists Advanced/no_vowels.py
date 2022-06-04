vowels = ['a', 'o', 'e', 'i', 'u']
word = input()
filtered_list = [ch for ch in word if ch not in vowels]

# for ch in word:
#     if ch not in vowels:
#         filtered_list.append(ch)

print("".join(filtered_list))