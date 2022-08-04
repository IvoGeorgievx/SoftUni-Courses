import re

count = int(input())
new_list = []

for _ in range(count):

    info = input()

    pattern = r'(@#+)([A-Z][a-zA-Z0-9]+[A-Z])(@#+)'
    result = re.match(pattern, info)

    if result is None or len(result.group()) < 10:
        print('Invalid barcode')
    else:
        extract_nums = re.findall(r'\d', result.group())

        if not extract_nums:
            print('Product group: 00')
        else:
            print(f"Product group: {''.join(extract_nums)}")




