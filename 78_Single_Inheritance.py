''' 
                Single Inheritance in Python
Single inheritance is a type of inheritance where a class 
inherits properties and behaviors from a single parent 
class. This is the simplest and most common form of 
inheritance.


                        Syntax
The syntax for single inheritance in Python is 
straightforward and easy to understand. To create a new 
class that inherits from a parent class, simply specify 
the parent class in the class definition, inside the 
parentheses, like this:

class ChildClass(ParentClass):
    # class body
'''

class Animal:

    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name, species= "dog")
        self.breed = breed
    
    def make_sound(self):
        print("Bark!")



a = Animal("animal","animallll")
a.make_sound()

d = dog("Dog","dogger")
d.make_sound()