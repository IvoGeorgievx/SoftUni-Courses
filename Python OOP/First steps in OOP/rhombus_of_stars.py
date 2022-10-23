size = int(input())
for i in range(size):
    spaces_count = size - 1 - i
    stars_count = i + 1
    print(' ' * spaces_count + '* ' * stars_count)

for i in range(size - 2, -1, -1):
    spaces_count = size - 1 - i
    stars_count = i + 1
    print(' ' * spaces_count + '* ' * stars_count)
