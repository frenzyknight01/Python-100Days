                                #Functions           1.Built-in Function    2.User-Define Function 
def CalculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a, b):
    pass #pass is use when we not work on that particular function then we can skip it. 

a = 6
b = 4
isGreater(a, b)
CalculateGmean(a, b)

c = 10
d = 15
isGreater(c, d)
CalculateGmean(c, d)    