input_count = int(input())

ss = set()

for i in range(input_count):
    chemicals = input().split(" ")
    for v in chemicals:
        if v not in ss:
            ss.add(v)

            print(v)
