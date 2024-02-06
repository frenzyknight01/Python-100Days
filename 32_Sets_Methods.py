                        #Sets Methods
#Joining sets

'''
The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.
'''
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2)) #union gives all values and remove dubble values 
s1.update(s2) #update gives adds item into the existing set from another set
print(s1,s2)

'''
The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2) #It gives common values only
print(cities3)

cities.intersection_update(cities2) #It gives intersection & update into the existing set from another set
print(cities)


'''
The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities.symmetric_difference_update(cities2)
print(cities)


'''
The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

'''
The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Dev", "Seoul", "Kabul", "Mad"}
print(cities.isdisjoint(cities2))#If First's set  values not present in another set returns true 

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))#If First's set  values present in another set returns False

'''
The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))

cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

cities3 = {"Tokyo", "Madrid","Berlin","Delhi"}
print(cities.issuperset(cities3))

'''
The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

cities3 = {"Tokyo", "Mad", "Berlin", "Delhi"}
print(cities2.issubset(cities3))


''' 
                    add()
If you want to add a single item to the set use the add() method.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki") #We can add only one element using  add function
print(cities)

'''
                    update()
If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2) #We can add multiple element using update function
print(cities)

'''
                remove()/discard()
We can use remove() and discard() methods to remove items form list.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)


'''
                        pop()
This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

'''
                        del
del is not a method, rather it is a keyword which deletes the set entirely.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities


'''
                    clear()
This method clears all items in the set and prints an empty set.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

'''
                Check if item exists
You can also check if an item exists in the set or not.
'''

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")