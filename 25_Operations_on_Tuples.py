                            #Operation of tuples
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

cou = countries.count("Finland") #We can count also
print(cou)

cou = countries.index("Finland") #We can also check index size
print(cou)

    #syntax :- tuple.index(element, start, end)
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3,5,8)
print('First occurrence of 3 is', res)