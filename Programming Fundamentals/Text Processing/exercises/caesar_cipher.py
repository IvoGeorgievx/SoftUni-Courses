def caesar_cipher(data):
    result = ''
    for i in data:
        result += chr(ord(i) + 3)

    print(result)


info = input()
caesar_cipher(info)