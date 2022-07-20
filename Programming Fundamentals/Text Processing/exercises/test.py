def rage_quit(data):
    unique_symbols = ''
    unique_symbol_count = 0
    ch_seq = ''
    nums = []
    for i in range(len(data) + 1):
        if data[i].isdigit():
            nums.append(data[i])
            prev_index = data[i]
            if prev_index.isdigit():
                nums.append(prev_index)
                unique_symbols += int(''.join(nums)) * ch_seq
            else:
                unique_symbols += int(''.join(nums)) * ch_seq
            ch_seq = ''
        else:
            ch_seq += data[i]
            nums.clear()
            if ch_seq not in unique_symbols:
                unique_symbol_count += 1

    print(f"Unique symbols used: {unique_symbol_count}")
    print(unique_symbols)


info = input()
rage_quit(info.upper())

