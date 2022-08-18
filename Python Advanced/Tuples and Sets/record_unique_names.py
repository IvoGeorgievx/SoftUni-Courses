names_count = int(input())

ss = set()

for _ in range(names_count):
    current_name = input()
    ss.add(current_name)

for name in ss:
    print(name)