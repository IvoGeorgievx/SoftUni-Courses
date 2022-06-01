def factorial(a):
    f = 1
    if a >= 1:
        for i in range(1, a + 1):
            f = f * i
        return f


first_n = int(input())
second_n = int(input())
result = factorial(first_n) / factorial(second_n)
print(f'{result:.2f}')