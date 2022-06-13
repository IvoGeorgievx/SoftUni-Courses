text = input().split(" ")
filtered = [i for i in text if (len(i)) % 2 == 0]
print('\n'.join(filtered))