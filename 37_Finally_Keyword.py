                        #Finally Clause
'''
The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.


Syntax:

try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation
'''

# try:
#     l = [1,5,6,7]
#     i = int(input("Enter the index: "))
#     print(l[i])
# except:
#     print("Some error occurred")

# finally:
#     print("I am always executed")
    

def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0

    finally:
        print("I am always executed") #finally always executed 
    # print("I am always executed") #It don't executed in function that's why we can use finally clause 

x = func1()
print(x)