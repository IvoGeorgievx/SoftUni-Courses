days_left = 5
pocket_money = float(input())
daily_sales = float(input())
expenses = float(input())
gift_price = float(input())

pocket_money_sum = days_left * pocket_money
daily_sales_sum = daily_sales * days_left
total_collected = daily_sales_sum + pocket_money_sum
total_money_left = total_collected - expenses
if total_money_left >= gift_price:
    print(f'Profit: {total_money_left:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {abs(total_money_left - gift_price):.2f} BGN.')

