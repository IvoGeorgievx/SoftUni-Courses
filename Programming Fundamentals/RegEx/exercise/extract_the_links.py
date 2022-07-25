import re


empty_list = []
pattern = r'(\bw{3})\.([a-zA-Z0-9\-]+)(\.([a-z]+))(\.?[a-z]*)+'

while True:

    text = input()

    if not text:
        break

    result = re.finditer(pattern, text)
    for i in result:
        print(i.group())






