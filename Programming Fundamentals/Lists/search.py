number = int(input())
given_word = input()
full_list = list()
filtered_list = list()

for _ in range(number):
    word = input()
    full_list.append(word)
    if given_word in word:
        filtered_list.append(word)

print(full_list)
print(filtered_list)


