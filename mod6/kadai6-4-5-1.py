def func():
    for x in range(10):
        yield x ** 2


for x in func():
    print(x*2)