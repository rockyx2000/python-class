try:
    dic = {'a':'赤', 'b':'青'}
    dic['c']

except KeyError:
    print("Keyerror が発生しました")