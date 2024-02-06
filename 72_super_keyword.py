'''
                    Super keyword in Python
The super() keyword in Python is used to refer to the 
parent class. It is especially useful when a class 
inherits from multiple parent classes and you want to call 
a method from one of the parent classes.

When a class inherits from a parent class, it can override 
or extend the methods defined in the parent class. 
However, sometimes you might want to use the parent class 
method in the child class. This is where the super() 
keyword comes in handy.

Here's an example of how to use the super() keyword in a 
simple inheritance scenario:
'''
class ParentClass:
    def parent_method(self):
        print("This is the parent method1.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Unknown2")
        super().parent_method()

    def child_method(self):
        print("This is the child method2.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()



                #we can also for that perpus dry principle
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
class Programmer(Employee):
    def __init__(self,name,id,lang):
        #We do not repeat 
        # self.name = name
        # self.id = id
        super().__init__(name,id) 
        self.lang = lang

c1 = Employee("Unknown",420)
c2 = Programmer("Known",2955,"Python")

print(c1.name)
print(c1.id)


print(c2.name)
print(c2.id)
print(c2.lang)
