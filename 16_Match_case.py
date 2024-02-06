x = int(input("Enter the value of x: "))

match x: # match case means when we are using switch case in c, c+. 
    case 0:
        print("x is zero")

    case 4:
        print("case is 4")

    case _:
        print(x)

                                                #Calculator using match case
A = int(input("Enter your first Value :"))
B = int(input("Enter your second value :"))
x = int(input("\n 1.Addition,\n 2.subtraction,\n 3.Multiplication, \n 4.Division,\n 5.Modulus, \n 6.Floor Division \n 7.Exponent \n"))

match x:
    case 1:
        ans1 = A+B
        print(f"Addition of {A} + {B} is {ans1}") # using F-string
    
    case 2:
        ans2 = A-B
        print(f"Subtraction of {A} - {B} is {ans2}")

    case 3:
        ans3 = A*B
        print(f"Multiplication of {A} * {B} is {ans3}")

    case 4:
        ans4 = A/B
        print(f"Division of {A} / {B} is {ans4}")

    case 5:
        ans5 = A%B
        print(f"Modulus of {A} % {B} is {ans5}")

    case 6:
        ans6 = A//B
        print(f"Addition of {A} // {B} is {ans6}")

    case 7:
        ans7 = A**B
        print(f"Exponent of {A} ** {B} is {ans7}")

    case _: # underscore('_') means default command. 
        print("Please choose valid1 number")