class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def show(self):
        print("Name  : ", self.name)
        print("Score : ", self.score)
    def score_up(self, upscr):
        self.score += upscr
        if self.score >= 100:
            self.score = 100


s1 = Student("赤山", 60)
s1.score_up(50)
s1.show()