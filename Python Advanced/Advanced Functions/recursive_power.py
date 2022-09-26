def recursive_power(n, p):
    if p == 0:
        return 1
    return n * recursive_power(n, p - 1)




# print(recursive_power(2, 10))
print(recursive_power(10, 100))