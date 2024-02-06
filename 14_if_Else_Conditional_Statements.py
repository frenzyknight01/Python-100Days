                      #if condition
a = int(input("Enter your age: "))
print("Your age is:", a)
# Conditional operators
# >, < , >= , <= , ==, !=
#print(a>18)
#print(a<=18)



#print(a==18)
#print(a!=18)
if(a>18):
    print("You can drive")
    print("Yes")
print("Ohh shit!!")


                    #If-Else condition
applePrice = 10 
budget = 200

if budget - applePrice > 50:
    print("Alexa, add 1kg Apples to the cart.")
else:
    print("Alexa, do not add apples to the cart.")



                    #elif Condition
num = int(input("Enter the value of num: "))
if num < 0:
    print("Number is negative.")
elif num == 0:
    print("Number is Zero.")
elif num == 999:
    print("Number is special.")
else:
    print("Number is positive.")



                #nested if condition
num = 18
if num < 0:
    print("Number is negative.")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10")
    elif num > 10 and num <= 20:
        print("Number is between 10-20")
else:
    print("Number is Zero")