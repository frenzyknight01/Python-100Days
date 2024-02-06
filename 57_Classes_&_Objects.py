                #Python Class and Objects
'''
A class is a blueprint or a template for creating objects, 
providing initial values for state (member variables or 
attributes), and implementations of behavior (member 
functions or methods). The user-defined objects are 
created using the class keyword.
'''
#Creating a Class:
class Person:
    name = "Frenzy"
    occupation = "Cyber Security investigator"
    networth = 1000000
    #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

    #It must be provided as the extra parameter inside the method definition.
    def info(self):
        print(f"{self.name} is a {self.occupation}")

#Creating an Object: 
Obj1 = Person()
Obj2 = Person()
Obj3 = Person()

Obj1.name = "Jayraj"
Obj1.occupation = "Gateway investigator"

Obj2.name = "Ravi"
Obj2.occupation = "Android Devloper"


Obj1.info()
Obj2.info()
Obj3.info() #When we not define objects value at that time self gives default class value

