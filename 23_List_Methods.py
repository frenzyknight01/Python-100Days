                                #List Methods
l = [35,3,6,1,9,5,18]
print(l)

l.sort() #This method sorts the list in ascending order. The original list is updated
print(l)

l.sort(reverse=True) # we can use condion also in parameter 
print(l) 

lst = [35,3,6,1,9,5,18] 
lst.reverse() #This method reverses the order of the list.
print(lst)

lst = [35,3,6,1,9,5,18] 
print(lst.index(6)) # This method returns the index of the first occurrence of the list item.

colors = ["voilet", "green", "indigo", "blue", "green","green"]
print(colors.count("green")) # Returns the count of the number of items with the given value.

colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy() #Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
print(colors)
print(newlist)

colors = ["voilet", "indigo", "blue"]
colors.append("green") #This method appends items to the end of the existing list.
print(colors)

colors = ["voilet", "indigo", "blue"]
colors.insert(2, "green")   #inserts item at index 2 #This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
print(colors)

colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)  #This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
print(colors)

#Concatenating two lists:
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2) # You can simply concatenate two lists to join two lists.





