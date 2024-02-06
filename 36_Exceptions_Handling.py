                        #Exception Handling 
'''
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.
'''

'''
Python try...except
try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception
'''


a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("Some imp lines of code")
print("End of program")




a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print("Sorry some error occurred")

print("Some imp lines of code")
print("End of program")



a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("Invalid Input")

print("Some imp lines of code")
print("End of program")


                    #Multiple error Handling
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])

except ValueError:
    print("Number entered is not an integer ")

except IndexError:
    print("Index Error")
    
