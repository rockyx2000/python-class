class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def show(self):
        print("Name  : ", self.name)
        print("Score : ", self.score)


s1 = Student("赤山", 60)
s1.show()

s2 = Student("井山", 70)
s2.show()