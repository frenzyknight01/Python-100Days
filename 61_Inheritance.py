                    #Inheritance in python
'''
When a class derives from another class. The child class 
will inherit all the public and protected properties and 
methods from the parent class. In addition, it can have 
its own properties and methods,this is called as 
inheritance.

Python Inheritance Syntax:

class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class

                Types of inheritance:
1.Single inheritance
2.Multiple inheritance
3.Multilevel inheritance
4.Hierarchical Inheritance
5.Hybrid Inheritance
'''

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.name} is {self.id}")


class Programmer(Employee):

    def showLanguage(self):
        print("The default language is Python")


e1 = Employee("Jayraj",420)
e1.showDetails()

e2 = Programmer("Ronak",230)
e2.showDetails()
e2.showLanguage()