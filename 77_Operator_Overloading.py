'''
        Operator Overloading: An Introduction
Operator Overloading is a feature in Python that allows 
developers to redefine the behavior of mathematical and 
comparison operators for custom data types. This means 
that you can use the standard mathematical operators (+, 
-, *, /, etc.) and comparison operators (>, <, ==, etc.) 
in your own classes, just as you would for built-in data 
types like int, float, and str.

        Why do we need operator overloading?
Operator overloading allows you to create more readable 
and intuitive code. For instance, consider a custom class 
that represents a point in 2D space. You could define a 
method called 'add' to add two points together, but using 
the + operator makes the code more concise and readable:

        How to overload an operator?
You can overload an operator in Python by defining special methods in your class. These methods are identified by their names, which start and end with double underscores (__). Here are some of the most commonly overloaded operators and their corresponding special methods:

+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__
'''


class Vector:
    def __init__(self,i,j,k):
        self.i = i 
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x): #Operator Overloading
        # return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k" #it gives string value
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k) #it gives vector 
    
v1 = Vector(3,4,5)
print(v1)

v2 = Vector(6,7,8)
print(v2)


print(v1 + v2)
print(type(v1 + v2))