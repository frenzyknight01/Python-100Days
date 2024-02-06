                            #List (Mutable)
marks = [3,5,7,"Harry",True]
print(marks)
print(type(marks))

                            #list index
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[:]) #print all element
print(marks[1:5:2]) #Syntax: listName[start : end : jumpIndex]


print(len(marks[3])) #positive index
print(marks[-3]) #Negative index
print(marks[len(marks)-3]) #positive index
print(marks[5-1])

if "Harry" in marks:
    print("Yes")
else:
    print("No")

                                #List Comprehension
'''
List comprehensions are used for creating new lists from other iterables like lists,
tuples, dictionaries, sets, and even in arrays and strings.
syntax List = [Expression(item) for item in iterable if Condition]

'''
lst1 = [i for i in range(10)]
lst2 = [i*i for i in range(10)]
lst3 = [i*i for i in range(10) if i%2==0] 
print(lst1)
print(lst2)
print(lst3)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)