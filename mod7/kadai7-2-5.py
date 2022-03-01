import abc

class Animal(abc.ABC):
    
    def show_type(self):
        print("種類は" , self.type , "です")
    @abc.abstractclassmethod
    def cry(self):
        pass
class Giraffe(Animal):
    def cry(self):
        print(" ")

g = Giraffe('キリン')
g.show_type