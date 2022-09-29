def even_odd(*args):
    even = []
    odd = []
    if args[-1] == 'even':
        for el in args[:-1]:
            if el % 2 == 0:
                even.append(el)
        return even
    else:
        for el in args[:-1]:
            if el % 2 != 0:
                odd.append(el)
        return odd

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
