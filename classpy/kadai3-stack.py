print("値を５つ入力してください。")

numt = []

for i in range(1,6):
    num = int(input("値を入力"))
    numt.append(num)

print("リストの中身は" + str(numt) + "です。")

print("スタックで表示します。")

for j in range(1,6):
    print(numt.pop(-1))

print("リストの中身は" + str(numt) + "です。")
print("以上です。")