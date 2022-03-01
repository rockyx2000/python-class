animal = {"cat":"猫", "dog":"犬", "bird":"鳥", "tiger":"トラ"}

name = input("英語で動物の名前を入力してください")

if name in animal:
    print(animal[name])
    
else:
    print("登録がありません")