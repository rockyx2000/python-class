menu = set()

menu |= {"カレー"}


menu |= {"オムライス", "ピザ"}

menu -= {"カレー", "ピザ"}

menu |= {"オムライス"}

menu -= {"トースト"}

#print(menu | {"パスタ"})

menu = menu - {"オムライス"}

print(menu)