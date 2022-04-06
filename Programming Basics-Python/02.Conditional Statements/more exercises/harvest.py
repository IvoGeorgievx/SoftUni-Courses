from math import ceil, floor

vineyard = int(input())
grape_per_sq_meter = float(input())
required_litres_wine = int(input())
workers = int(input())

grape_total = vineyard * grape_per_sq_meter
wine_sum = (grape_total * 0.4) / 2.5

if wine_sum >= required_litres_wine:
    wine_sum_left = wine_sum - required_litres_wine
    wine_per_person = wine_sum_left / workers
    print(f'Good harvest this year! Total wine: {floor(wine_sum)} liters.')
    print(f'{ceil(wine_sum_left)} liters left -> {ceil(wine_per_person)} liters per person.')
elif wine_sum <= required_litres_wine:
    wine_needed = required_litres_wine - wine_sum
    print(f'It will be a tough winter! More {floor(wine_needed)} liters wine needed.')









