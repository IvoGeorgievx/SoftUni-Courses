expression = input()

s = []

for i in range(len(expression)):
    if expression[i] == '(':
        s.append(i)
    elif expression[i] == ')':
        end_index = i
        start_index = s.pop()
        print(expression[start_index:end_index + 1])