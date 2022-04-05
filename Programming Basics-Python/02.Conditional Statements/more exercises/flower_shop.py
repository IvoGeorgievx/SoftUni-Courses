from math import ceil, floor

magnolias_count = int(input())
zyumbyul_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

magnolias_price = 3.25
zyumbyul_price = 4
rose_price = 3.50
cactus_price = 8

total_income_without_tax = (magnolias_price * magnolias_count) + \
                           (zyumbyul_price * zyumbyul_count) + \
                           (rose_price * roses_count) + \
                           (cactus_price * cactus_count)
total_income_with_taxes = total_income_without_tax - (total_income_without_tax * 0.05)
if gift_price <= total_income_with_taxes:
    print(f'She is left with {floor(total_income_with_taxes - gift_price)} leva.')
else:
    print(f'She will have to borrow {ceil(gift_price - total_income_with_taxes)} leva.')

