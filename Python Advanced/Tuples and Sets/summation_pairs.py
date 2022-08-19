nums = list(map(int, input().split()))
target = int(input())

result_nums = set()
values = {}

for value in nums:
    if value in result_nums:
        p1 = value
        p2 = values[value]
        print(f'{p1} + {p2} = {target}')
    else:
        result_nums.add(target - value)
        values[target - value] = value



