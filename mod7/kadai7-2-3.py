class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def show(self):
        print('Name    : ', self.name)
        print('Score   : ', self.score)
class Worker:
    def __init__(self, name, score, salary):
        Student.__init__(self, name, score)
        self.salary = salary
    def nensyu(self):
        print("名前は  :  ", self.name)
        print("月収は  :  ", self.salary)
        self.__check_income()
    def __check_income(self):
        self.salary *= 12
        print("年収は  :  ", self.salary)
class WorkerStudent(Student, Worker):
    def __init__(self, name, score, salary):
        Student.__init__(self,name,score)
        Worker.__init__(self, name, score, salary)      

        
ws = WorkerStudent('宇山', 80, 200000)
ws.show()
ws.nensyu()