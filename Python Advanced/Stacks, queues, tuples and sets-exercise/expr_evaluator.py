from collections import deque

expression = input().split()
nums = deque()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

for ch in expression:
    if ch in '*/-+':
        while len(nums) > 1:
            left = nums.popleft()
            right = nums.popleft()
            result = operations[ch](left, right)
            nums.appendleft(result)
    else:
        nums.append(int(ch))

print(nums.popleft())