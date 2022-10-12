def words_sorting(*args, **kwargs):
    dd = {}
    for arg in args:
        dd[arg] = 0
        current_sum = 0
        for i in arg:
            current_sum += ord(i)
        dd[arg] = current_sum
    total_sum = 0
    for sum in dd.values():
        total_sum += sum

    sorted_dd = [f'{key} - {value}' for key, value in sorted(dd.items(), key=lambda x: x if total_sum % 2 == 0 else -x[1])]
    return '\n'.join(sorted_dd)


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
