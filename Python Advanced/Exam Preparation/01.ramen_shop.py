from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while bowls_of_ramen and customers:

    current_ramen = bowls_of_ramen.pop()
    current_customer = customers.popleft()

    if current_customer == current_ramen:
        continue

    elif current_ramen > current_customer:
        current_ramen -= current_customer
        bowls_of_ramen.append(current_ramen)

    elif current_customer > current_ramen:
        current_customer -= current_ramen
        customers.appendleft(current_customer)

if not customers and not bowls_of_ramen:
    print("Great job! You served all the customers.")

elif customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
elif bowls_of_ramen:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}")

