celsius = float(input())
# To convert temperatures in degrees Celsius to Fahrenheit,
# multiply by 1.8 (or 9/5) and add 32.

c_to_f = celsius * 1.8 + 32
formatted_f = "{:.2f}".format(c_to_f)
print(formatted_f)
