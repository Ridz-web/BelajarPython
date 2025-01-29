x = 20 # berada di scope global

def x_scope():
    global x #mengambil variabel yang ada diluar function
    x += 5 # menambah variabel x di scope global sebanyak 5 = 25
    print(f"x_scope, {x}")

def outer_function():
    x = 10 # variabel x baru
    def inner_function():
        nonlocal x # mengambil variabel x yang ada di dalam outer_function
        x += 5 # menambah varibel x di scope nonlocal/di outher_function sebanyak 5 = 15
        print(f"inner function, {x}")
    inner_function()
    print("outer function,", x)


x_scope()
outer_function()