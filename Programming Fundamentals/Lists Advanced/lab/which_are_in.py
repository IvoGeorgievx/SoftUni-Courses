substrings = input().split(", ")
strings = input()

filtered_list = [el for el in substrings if el in strings]
print(filtered_list)