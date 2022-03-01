class Animal:
    def cry(self):
        print('△◎※□')

class Cat(Animal):
    def cry(self):
        print('ニャー')


a = Cat()
a.cry()

#　Animalクラスを継承したCatクラスを使って
#　ニャーと表示してみる

#　同様に、ワンワンと表示するDogクラスを作って
#　実行してみる

#　Dogクラスのcryメソッドは、
#　実行時に、引数として鳴き声を渡すようにする

# d = Dog()
# d.cry('バウワウ')
