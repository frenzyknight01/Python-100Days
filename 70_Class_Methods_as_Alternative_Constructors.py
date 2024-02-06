'''
            Class Methods as Alternative Constructors
In object-oriented programming, the term "constructor" 
refers to a special type of method that is automatically 
executed when an object is created from a class. The 
purpose of a constructor is to initialize the object's 
attributes, allowing the object to be fully functional and 
ready to use.

However, there are times when you may want to create an 
object in a different way, or with different initial 
values, than what is provided by the default constructor. 
This is where class methods can be used as alternative 
constructors.

A class method belongs to the class rather than to an 
instance of the class. One common use case for class 
methods as alternative constructors is when you want to 
create an object from data that is stored in a different 
format, such as a string or a dictionary. For example, 
consider a class named "Person" that has two attributes: 
"name" and "age". The default constructor for the class 
might look like this:

'''
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

e1 = Employee("Unknown",12000)
print(e1.name)
print(e1.salary)

string = "Known-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)
