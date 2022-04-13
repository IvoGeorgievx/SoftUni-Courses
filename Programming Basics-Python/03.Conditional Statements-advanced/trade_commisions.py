city_name = input()
sales_volume = float(input())
commission = 0

if 0 <= sales_volume <= 500:
    if city_name == 'Sofia':
        commission = 0.05
    elif city_name == 'Varna':
        commission = 0.045
    elif city_name == 'Plovdiv':
        commission = 0.055
if 500 < sales_volume <= 1000:
    if city_name == 'Sofia':
        commission = 0.07
    elif city_name == 'Varna':
        commission = 0.075
    elif city_name == 'Plovdiv':
        commission = 0.08

if 1000 < sales_volume <= 10000:
    if city_name == 'Sofia':
        commission = 0.08
    elif city_name == 'Varna':
        commission = 0.1
    elif city_name == 'Plovdiv':
        commission = 0.12

if sales_volume > 10000:
    if city_name == 'Sofia':
        commission = 0.12
    elif city_name == 'Varna':
        commission = 0.13
    elif city_name == 'Plovdiv':
        commission = 0.145

if commission == 0:
    print('error')
else:
    income = sales_volume * commission
    print(f'{income:.2f}')











