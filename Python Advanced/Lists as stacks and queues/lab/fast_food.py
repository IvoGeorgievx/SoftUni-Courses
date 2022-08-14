from collections import deque

food_quantity = int(input())
order_quantity = deque(map(int, input().split()))

print(max(order_quantity))


while order_quantity:

    if food_quantity < int(order_quantity[0]) and order_quantity:
        break
    food_quantity -= int(order_quantity.popleft())

complete_stack = []

if len(order_quantity) <= 0:
    print('Orders complete')
else:
    while order_quantity:
        asd = order_quantity.popleft()
        complete_stack.append(str(asd))
    print(f"Orders left: {' '.join(complete_stack)}")




