                    #local and global variables

'''
#   Before we dive into the differences between local and global variables, let's first recall what a variable is in Python.

#   A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns.

#   On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.
'''

# x = 4 #global varible
# print(x)

# def hello():
#     x = 5 #local varible
#     print(f"The local x is {x}")
#     print("Hello harry")

# print(f"The global x is {x}")
# hello()
# print(f"The global x is {x}")




x = 10 #global variable

def my_function():
    global x #it can use for using global variable
    x = 4 # This will change the value of the global variable x
    y = 5 #local variable
    print(y)

print(f"With out converting by global {x}")
my_function()
print(f"converting by global {x}")
# print(y) #this will cause an error because y is a local variable and is not accessible outside of the function

