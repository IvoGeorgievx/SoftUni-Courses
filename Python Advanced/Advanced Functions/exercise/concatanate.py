def concatenate(*args, **kwargs):
    empty_str = ''
    for el in args:
        empty_str += el
    empty_str = empty_str.strip()

    for key, value in kwargs.items():
        if key in empty_str:
            empty_str = empty_str.replace(key, value)
    return empty_str





print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))