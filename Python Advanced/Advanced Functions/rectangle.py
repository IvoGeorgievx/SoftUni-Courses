def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * length + 2 * width

    if type(length) == str or type(width) == str:
        return 'Enter valid values!'
    else:
        return f'''Rectangle area: {area()}
Rectangle perimeter: {perimeter()}'''


print(rectangle(2, 10))
print(rectangle('2', 10))
