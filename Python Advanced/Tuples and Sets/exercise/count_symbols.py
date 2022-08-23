text = input()

dd = {}

for ch in text:
    if ch not in dd:
        dd[ch] = 1
    else:
        dd[ch] += 1

sorted_dict = {key: value for key, value in sorted(dd.items())}

for key, value in sorted_dict.items():

    print(f'{key}: {value} time/s')
