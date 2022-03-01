def multi(*number):
    s = 1
    for n in number:
        s *= n
    
    return s

print(multi(2, 3, 4, 5))
print(multi(100, 30))