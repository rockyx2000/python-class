class Animal:
    def __init__(self, type):
        self.type = type
    def show_type(self):
        print("種類は" , self.type , "です")
    def cry(self):
        pass
class Cat(Animal):
    def __init__(self, type):
        Animal.__init__(self, type)
    def cry(self):
        print("ニャー")
class Dog(Animal):
    def __init__(self, type):
        Animal.__init__(self, type)
    def cry(self):
        print("ワン")


c = Cat('三毛')
c.show_type() 
c.cry()
d = Dog('豆柴')
d.show_type() 
d.cry()