def test2(*x, **y):
    print(x)
    print(y)
    return ""


test2(1,2,3)

test2(a = 4, b = 5, c = 6)

test2(1,2,3,a = 4, b = 5, c = 6)

#test2(a = 4, b = 5, c = 6,1,2,3)