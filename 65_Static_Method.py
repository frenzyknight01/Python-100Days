'''
                        Static methods
Static methods in Python are methods that belong to a
 class rather than an instance of the class. They are 
 defined using the @staticmethod decorator and do not have 
 access to the instance of the class (i.e. self). They are 
 called on the class itself, not on an instance of the 
 class. Static methods are often used to create utility 
 functions that don't need access to instance data.
'''

class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num += n

    @staticmethod
    def add(a,b):
        return a + b

a = Math(10)
print(a.num)
a.addtonum(50)
print(a.num)

print(a.add(7,2)) #normally we can access by instance 
print(Math.add(10,2)) #using static method we can access by class name also
