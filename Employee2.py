class Person:
    a = 100
    def __init__(self,firstname,lastname):
        self.first = firstname
        self.last = lastname

    def Name(self):
        return self.first + " " + self.last

class Employee(Person):

    def __init__(self,firstname,lastname,cname):
        Person.__init__(self,firstname,lastname)
        self.companyname = cname

    def GetCompanyInfo(self):
        return self.Name()+" "+self.companyname

emp = Employee('san','deep','google')
print emp.GetCompanyInfo()
print emp.Name()
per = Person('john','hop')
print per.Name()