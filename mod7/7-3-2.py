try:
    dic = {'a':'赤', 'b':'青'}
    #dic['c']
    dic['a']

except KeyError:
    print("Keyerror が発生しました")
    
else:
    print("Keyerror は発生しませんでした")
    
finally:
    print(dic)