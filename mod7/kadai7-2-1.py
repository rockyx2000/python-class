class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def show(self):
        print('Name    : ', self.name)
        print('Score   : ', self.score)
class Unten:
    def __init__(self, name, score, vehicle):
        Student.__init__(self, name ,score)
        self.vehicle = vehicle
    def show(self):
        Student.show(self)
        print("Vehicle : ", self.vehicle)
    def cost(self):
        print("メンテナンス代とガソリン代")
        
        
u = Unten('赤山', 60, 'バイク')
u.show()
u.cost()