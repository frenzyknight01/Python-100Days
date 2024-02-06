'''
            Instance vs class variables
In Python, variables can be defined at the class level or
 at the instance level. Understanding the difference 
 between these types of variables is crucial for writing 
 efficient and maintainable code.


                    Class Variables
Class variables are defined at the class level and are 
shared among all instances of the class. They are defined 
outside of any method and are usually used to store 
information that is common to all instances of the class. 
For example, a class variable can be used to store the 
number of instances of a class that have been created.
'''

class Employee:
    companyName = "Apple" #Class variables
    noOfEmployees = 0 

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1

    def showDetails(self):
        print(f"The Name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")
    
emp1 = Employee("Unknown")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India" #Instance variable
emp1.showDetails()
Employee.companyName = "Google"  #Class variable
print(Employee.companyName)


emp2 = Employee("Karan")
emp2.companyName = "Nestle" #Instance varible
emp2.showDetails()