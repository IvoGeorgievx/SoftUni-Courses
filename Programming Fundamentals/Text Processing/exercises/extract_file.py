def extract_file(data):

    last_element = data[-1].split(".")
    file_name = last_element[0]
    file_extension = last_element[1]
    print(f'File name: {file_name}')
    print(f'File extension: {file_extension}')


info = input().split("\\")
extract_file(info)
