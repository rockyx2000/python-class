def test3(*x, **y):
    for key in x:
        print(key)
    
    t = y  
    for k,v in t.items():
        print(k,v)



test3(1, 2, 3)

test3(a = 4, b = 5, c = 6)

test3(1,2,3,a = 4, b = 5, c = 6)