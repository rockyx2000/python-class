class Student:
    def show(self):
        print("Name  : ", self.name)
        print("Score : ", self.score)


s1 = Student()
s1.name = "赤山"
s1.score = 60
s1.show()


s2 = Student()
s2.name = "井山"
s2.score = 70
s2.show()