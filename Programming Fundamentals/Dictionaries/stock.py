elements = input().split(" ")
my_dict = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    my_dict[key] = int(value)

searched_product = input().split(" ")

for product in searched_product:
    if product in my_dict:
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

