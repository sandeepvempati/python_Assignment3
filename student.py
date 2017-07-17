class Student:
    def __init__(self):
        pass
    def getString(self):
        name = raw_input()
        self.name = name
    def printString(self):
        return self.name.upper()

class Stu(Student):
    def __init__(self,):
        Student.__init__(self)

s = Stu()
print s.getString()
print s.printString()



