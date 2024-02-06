                        #Enumerate
'''
Enumerate function in python
The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:
'''


marks = [12,56,85,3,99,45,23]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#        print("Meet, awesome")
#     index += 1


for index,mark in enumerate(marks, start=1):
    print(index,mark)
    if(index == 3):
       print("Meet, awesome")