change = float(input())
coin_count = 0

while change > 0:

    if change >= 2:
        change -= 2

    elif change >= 1:
        change -= 1

    elif change >= 0.50:
        change -= 0.50

    elif change >= 0.20:
        change -= 0.20

    elif change >= 0.10:
        change -= 0.10

    elif change >= 0.05:
        change -= 0.05

    elif change >= 0.02:
        change -= 0.02

    elif change >= 0.01:
        change -= 0.01

    change = round(change, 2)
    coin_count += 1
print(coin_count)
