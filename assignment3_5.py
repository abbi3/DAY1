#Relationships

class person:
    name: object = None
    def __int__(self,name):
        self.name = name
    def getname(self):
        return self.name

class student(person):
    def __int__(self,id,name):
        person.__int__(self,name)
        self.id = id
    def printid(self):
        return self.id
    def printname(self):
        return self.name
    @staticmethod
    def staticMethod():
        print("this is static class method")
    @classmethod
    def classmethod(cls):
        print("this is class method")
p = person()
print(p.getname())

s = student(2,"56")
s = student.printid(s)
s =student.printname()




