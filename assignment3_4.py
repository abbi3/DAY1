#inheritence concepts
class A(object):
    def __init__(self):
        print("this is init method ")
    def sum(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def addsum(self,adsum):
        self.addsum=adsum
        adsum = self.a+self.b

    def addallsum(self,adddd):
        self.adddd=adddd
        adddd = self.a + self.b+self.c
        return adddd

a = A()
a.sum()
a.addsum()
a.addallsum()
