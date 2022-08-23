n = set()
m = set()

inpu = list(map(int, input().split()))

n_length = inpu[0]
m_length = inpu[1]

for _ in range(n_length):
    n_nums = int(input())
    n.add(n_nums)

for _ in range(m_length):
    m_nums = int(input())
    m.add(m_nums)

for i in n.intersection(m):
    print(i)