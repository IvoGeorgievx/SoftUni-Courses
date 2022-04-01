movie_budget = float(input())
extras_number = int(input())
extras_dressing_cost = float(input())

decor = movie_budget * 0.1
extras_dressing_total = extras_number * extras_dressing_cost

if extras_number > 150:
    extras_dressing_total = extras_dressing_total - (extras_dressing_total * 0.1)

if decor + extras_dressing_total > movie_budget:
    movie_budget = abs(movie_budget - decor - extras_dressing_total)
    print('Not enough money!')
    print(f'Wingard needs {movie_budget:.2f} leva more.')
else:
    movie_budget = movie_budget - (decor + extras_dressing_total)
    print('Action!')
    print(f'Wingard starts filming with {movie_budget:.2f} leva left.')



