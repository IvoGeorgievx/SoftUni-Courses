count = int(input())
total_nums = []
for i in range(count):
    command = input()
    if command.startswith('1'):
        exploded = command.split()
        current_num = exploded[1]
        total_nums.append(int(current_num))
    elif command == '2' and total_nums:
        total_nums.pop()
    elif command == '3' and total_nums:
        print(max(total_nums))
    elif command == '4' and total_nums:
        print(min(total_nums))

reversed_stack = []

while total_nums:
    asd = total_nums.pop()
    reversed_stack.append(str(asd))

print(f'{", ".join(reversed_stack)}')