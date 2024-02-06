                            #Different types of function arguments 
                                    #1.Default Arguments 
'''
We can provide a default value while creating a function.
This way the function assumes a default value even
if a value is not provided in the function call for that argument.
'''
def average(a=9, b=4): 
    cal = (a+b/ a**b)
    print(cal)

def name(fname, mname = "Jhon", lname = "Whatson"): # IT Called required arguments also in default arguments
    print("Hello,", fname, mname, lname)


name("Amy")
average()
average(a=10) # we can also define new value


                                    #2.Keyword Arguments
'''
We can provide arguments with key = value,
this way the interpreter recognizes the arguments by the parameter name.
 Hence, the the order in which the arguments are passed does not matter.
'''

def average(a,b):
    cal = (a+b/a**b)
    print(cal)

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)


name(mname = "Peter", lname = "Wesker", fname = "Jade")
average(b=10,a=5) # we can define variable value unorder also run this task


                                    #3.Required Arguments
"""
# In case we don’t pass the arguments with a key = value syntax,
then it is necessary to pass the arguments in the correct positional order and
the number of arguments passed should match with actual function definition.
"""

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("RAVI","Peter", "Quill")

                                #4.Variable Length Arguments
'''Sometimes we may need to pass more arguments than those defined in the actual function.
This can be done using variable-length arguments.
'''
#There are two ways to achieve this:
''' 1. Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function.
The function accesses the arguments by processing them in the form of tuple.
'''

def average(*numberes): # '*' is for tuple 
    print(type(numberes))
    sum = 0
    for i in numberes:
        sum += i
    print("Average is: ", sum / (len(numberes)))

average(10,20, 30)

''' 2.Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function.
The function accesses the arguments by processing them in the form of dictionary.
'''

def name(**name): # '** 'is for dictionary
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

                                #Return statement
def average(*numberes): # '*' is for tuple 
    print(type(numberes))
    sum = 0
    for i in numberes:
        sum += i
    return sum / (len(numberes))

c = average(10,20, 30)
print(c)