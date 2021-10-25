#%%
chars = ["n","a","h","a"]

print("リスト chars を作成、初期値を naha にする \n", chars)

#%%
chars.reverse()

print("逆順にする \n",chars)

#%%
#to_remove = ["a"]
chars = [i for i in chars if i !='a']

print("aを2つ削除 \n",chars)
# %%
chars.insert(1,"o")

print("2文字目に o を挿入 \n",chars)

#%%
chars.append("e")

print("末尾に e を追加 \n",chars)

#%%
chars.sort()

print("アルファベットの昇順にする \n",chars)

