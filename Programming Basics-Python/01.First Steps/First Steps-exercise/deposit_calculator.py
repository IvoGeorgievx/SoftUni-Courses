deposited_amount = float(input())
deposit_due = int(input())
annual_interest = float(input())

due_interest = deposited_amount * (annual_interest / 100)
monthly_interest = due_interest / 12
total_amount = deposited_amount + deposit_due * monthly_interest
print(total_amount)










