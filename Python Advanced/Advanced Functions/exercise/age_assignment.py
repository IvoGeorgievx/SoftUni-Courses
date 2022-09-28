def age_assignment(*args, **kwargs):
    name_dict = {}
    for name in args:
        first_letter = name[0]
        age = kwargs[first_letter]
        name_dict[name] = age
    sorted_dict = [f'{key} is {value} years old.' for key, value in (sorted(name_dict.items(), key=lambda x: x[0]))]
    return '\n'.join(sorted_dict)



print(age_assignment("Peter", "George", G=26, P=19))