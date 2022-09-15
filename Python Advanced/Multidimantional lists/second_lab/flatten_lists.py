expression = input().split("|")

ll = []

for idx in range(len(expression) - 1, -1, -1):
    current_elements = expression[idx].strip().split()
    ll.extend(current_elements)


print(*ll)


