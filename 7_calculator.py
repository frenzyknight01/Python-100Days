A = int(input("Enter your first Value :"))
B = int(input("Enter your second value :"))
valid = int(input("\n 1.Addition,\n 2.subtraction,\n 3.Multiplication, \n 4.Division,\n 5.Modulus, \n 6.Floor Division \n 7.Exponent \n"))


if valid == 1:
    ans1 = A+B
    print(f"Addition of {A} and {B} is {ans1}") # using F-string

elif valid == 2:
    ans2 = A-B
    print(f"Subtraction of {A} and {B} is {ans2}")

elif valid == 3:
    ans3 = A*B
    print(f"Multiplication of {A} and {B} is {ans3}")

elif valid == 4:
    ans4 = A/B
    print(f"Division of {A} and {B} is {ans4}")

elif valid == 5:
    ans5 = A%B
    print(f"Modulus of {A} and {B} is {ans5}")

elif valid == 6:
    ans6 = A//B
    print(f"Floor Division of {A} and {B} is {ans6}")

elif valid == 7:
    ans7 = A**B
    print(f"Exponent of {A} and {B} is {ans7}")