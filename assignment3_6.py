#exercise
class pets:
    dogs = []
    def __init__(self,dogs):
        self.dogs = dogs

class dogs:
    speices = 'mammals'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getname(self):
        print(self.name)
    def getage(self):
        print(self.age)

class tom(dogs):
    def desc(self):
        print("tom ")

d = dogs("a",2)
d1 = dogs("b",3)
d2 = dogs("c",5)
mypets = pets([d,d1,d2])
print("i have", len(mypets.dogs),"dogs")
t = tom()
t.desc()

