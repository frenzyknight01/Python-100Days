''' 
            Hybrid Inheritance
Hybrid inheritance is a combination of multiple 
inheritance and single inheritance in object-oriented 
programming. It is a type of inheritance in which multiple 
inheritance is used to inherit the properties of multiple 
base classes into a single derived class, and single 
inheritance is used to inherit the properties of the 
derived class into a sub-derived class.

In Python, hybrid inheritance can be implemented by 
creating a class hierarchy, in which a base class is 
inherited by multiple derived classes, and one of the 
derived classes is further inherited by a sub-derived 
class.

                        Syntax
The syntax for implementing Hybrid Inheritance in Python 
is the same as for implementing Single Inheritance, 
Multiple Inheritance, or Hierarchical Inheritance.

Here's the syntax for defining a hybrid inheritance class 
hierarchy:

class BaseClass1:
  # attributes and methods
class BaseClass2:
  # attributes and methods
class DerivedClass(BaseClass1, BaseClass2):
  # attributes and methods
'''
                    #1st Example
# Code block
# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

# Derived class
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def show_details(self):
        super().show_details()
        print("Bonus:", self.bonus)

# Hybrid class
class CEO(Manager, Employee):
    def __init__(self, name, salary, bonus, stock):
        super().__init__(name, salary, bonus)
        self.stock = stock

    def show_details(self):
        super().show_details()
        print("Stock:", self.stock)

# Creating objects
emp = Employee("Alice", 50000)
mgr = Manager("Bob", 80000, 10000)
ceo = CEO("Charlie", 100000, 20000, 5000)

# Calling methods
emp.show_details()
print()
mgr.show_details()
print()
ceo.show_details()

                    #2nd Example

class GrandPa:
    def __init__(self):
        print("Grand Pa")

class Father(GrandPa):
    def __init__(self):
        super().__init__()
        print("Father")

class Mother(GrandPa):
    def __init__(self):
        super().__init__()
        print("Mother")


class child(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Child")

c = child()

'''
                Hierarchical Inheritance
Hierarchical Inheritance is a type of inheritance in 
Object-Oriented Programming where multiple subclasses 
inherit from a single base class. In other words, a single 
base class acts as a parent class for multiple subclasses. 
This is a way of establishing relationships between 
classes in a hierarchical manner.

                    Syntax
class BaseClass:
  pass

class D1(BaseClass):
  pass

class D2(BaseClass):
  pass

class D3(D1):
  pass
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "is making a sound.")

# Derived class 1
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name, "is meowing.")

# Derived class 2
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name, "is barking.")

# Creating objects
a = Animal("Leo")
c = Cat("Luna")
d = Dog("Max")

# Calling methods
a.speak()
c.speak()
d.speak()
