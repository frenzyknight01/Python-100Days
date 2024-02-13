                        #How Import works 
'''
How importing in python works
'''
# from Subfile44 import welcome,Unknown
import Subfile44 as sub
sub.welcome()
print(sub.Unknown)


# import math

# result = math.sqrt(9)
# print(result)

                    #from keyword
# from math import sqrt,pi

# result = sqrt(5)
# print(result)

                    #importing everything
# from math import * # It means all function implement 

# result = sqrt(5) * pi
# print(result)

                    #The "as" keyword
# from math import sqrt as s,pi as p

# result = s(5) * p
# print(result)



# import math as m

# result = m.sqrt(5) * m.pi 
# print(result)

'''
The dir function
Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.
'''

# import math

# print(dir(math))


# import math
# print(math.nan, type(math.nan))

                #We can also import by own file and functions 
                
