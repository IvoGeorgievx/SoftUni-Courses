x = 'global'


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print("inner:", x)

    def global_change():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    global_change()


print(x)
outer()
print(x)