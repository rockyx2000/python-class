def week(index):
    days = ["月", "火", "水", "木", "金"]
    
    yield days[index]


for i in range(2):
    for p in week(i):
        print(p)