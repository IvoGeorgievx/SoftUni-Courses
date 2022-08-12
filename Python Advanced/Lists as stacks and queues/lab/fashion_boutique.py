stack = []

nums = list(map(int, input().split()))
capacity = int(input())
hanger_counter = 1
fresh_capacity = capacity

while len(nums) > 0:
    if fresh_capacity >= 0 and nums[-1] <= fresh_capacity:
        fresh_capacity -= nums.pop()
    else:
        hanger_counter += 1
        fresh_capacity = capacity

print(hanger_counter)