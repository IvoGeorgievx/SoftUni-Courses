new_string = lambda string, multiplier: f'{current_string * multiplier}'
current_string = input()
multiplier = int(input())
print(new_string(current_string, multiplier))