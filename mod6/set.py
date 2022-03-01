#空の集合を定義
div12 = set()
div18 = set()

#12の約数を集合へ追加
for i in range(1,13):
    if 12 % i == 0:
        div12 |= {i}
        

#18の約数を集合へ追加
for p in range(1,19):
    if 18 % p == 0:
        div18 |= {p}
        

#div12とdiv18の集合の積集合を出力
print("12と18の公約数 :",div12 & div18)