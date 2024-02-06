                    #Raising custom error
'''
Raising Custom errors:

In python, we can raise custom errors by using the raise keyword.

Defining Custom Exceptions
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:

class CustomError(Exception):
  # code ...
  pass

try:
  # code ...

except CustomError:
  # code...
'''


a = int(input("Enter any value between 4 and 9: "))

if(a<4 or a>9):
    raise ValueError("Value should be between 4 and 9")


# types of different error
NameError
ValueError
IndexError
KeyError
MemoryError
NotImplementedError
OverflowError
RecursionError
ReferenceError
RuntimeError
StopIteration
SyntaxError
IndentationError
TabError
SystemError
