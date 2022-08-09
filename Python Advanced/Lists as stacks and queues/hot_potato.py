from collections import deque

kids = deque(input().split(" "))
toss_count = int(input())
current_count = 0

while len(kids) > 1:
    current_count += 1

    kid = kids.popleft()
    if current_count < toss_count:
        kids.append(kid)
    else:
        print(f'Removed {kid}')
        current_count = 0
print(f'Last is {kids[0]}')