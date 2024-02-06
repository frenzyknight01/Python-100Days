'''
                    Class Methods
Python Class Methods: An Introduction
In Python, classes are a way to define custom data types 
that can store data and define functions that can 
manipulate that data. One type of function that can be 
defined within a class is called a "method." In this blog 
post, we will explore what Python class methods are, why 
they are useful, and how to use them.


                What are Python Class Methods?
A class method is a type of method that is bound to the 
class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the 
class. Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the 
function is always "cls," which represents the class itself.

                Why Use Python Class Methods?
Class methods are useful in several situations. For example, you might want to create a factory method that 
creates instances of your class in a specific way. You 
could define a class method that creates the instance and 
returns it to the caller. Another common use case is to 
provide alternative constructors for your class. This can 
be useful if you want to create instances of your class in 
multiple ways, but still have a consistent interface for 
doing so.


class ExampleClass:
    @classmethod
    def factory_method(cls, argument1, argument2):
        return cls(argument1, argument2)
'''
class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod #When we use this method gives class variable
    def ChangeCompany(cls,newCompany):
        cls.company = newCompany

    
e1 = Employee()
e1.name = "Unknown"
e1.show()
e1.ChangeCompany("Maybach") #IT gives instance variable only
e1.show()
# print(Employee.company) #you can see at the end in gives class varible