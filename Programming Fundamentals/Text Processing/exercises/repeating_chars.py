def repeating_chars():
    data = input()
    result = ''

    for i in range(len(data)):
        if i == 0:
            result += data[i]
        else:
            if data[i] != data[i - 1]:
                result += data[i]

    print(result)


repeating_chars()
