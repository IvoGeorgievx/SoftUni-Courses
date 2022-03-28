vegetable_price = float(input())
fruit_price = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

vegetable_sum = vegetable_kg * vegetable_price
fruit_sum = fruit_kg * fruit_price
total_sum = (vegetable_sum + fruit_sum) / 1.94
formatted_sum = "{:.2f}".format(total_sum)
print(formatted_sum)




