def emoticon_finder(data):
    result = [data[i] + data[i + 1] for i in range(len(data)) if data[i] == ':' and data[i + 1] != " "]
    print('\n'.join(result))


data = input()
emoticon_finder(data)
