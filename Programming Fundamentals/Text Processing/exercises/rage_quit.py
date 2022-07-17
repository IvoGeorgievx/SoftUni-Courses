def rage_quit(data):
    unique_symbols = ''
    unique_symbol_count = 0
    ch_seq = ''
    for i in data:
        if i.isdigit():
            number = i
            unique_symbols += int(number) * ch_seq
            ch_seq = ''
        else:
            ch_seq += i
            if ch_seq not in unique_symbols:
                unique_symbol_count += 1

    print(f"Unique symbols used: {unique_symbol_count}")
    print(unique_symbols)


info = input()
rage_quit(info.upper())

