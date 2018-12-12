#inheritence

'''class animal():
    def eat(self):
        print("eat self")
class dog(animal):
     def eat(self):
         print("other animals and things")
d=dog()
d.eat()'''

#multilevel inheritence
'''class animals:
    def animals(self):
        print("animals are nice")
class dog(animals):
    def dog(self):
        print("this is dog class")
    def bark(self):
        print("Barks")
class babydog(dog):
    def babydog(self):
        print("this is baby dogs place")
    def look(self):
        print("this babydog is cute ")
a = animals()
d = dog()
d.bark()
b = babydog()
b.babydog()
b.look() '''


'''class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")


class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")


class Third(Second, First):
    def __init__(self):
        super(Third, self).__init__()
        print("third")
Third();'''