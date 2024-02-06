fruit = "Mango"
print(len(fruit))

print(fruit[0:4]) #including 0 but not 4
print(fruit[1:4]) #including 1 but not 4
print(fruit[:5]) 
print(fruit[0:-3])
print(fruit[0:len(fruit)-3]) # 5 - 3 = 2
print(fruit[-1:len(fruit)-3]) # 5-1 = 4 : 5-3 = 2  4:2 NOT VALID (give blankspace)  
print(fruit[-3:-1]) # 5-3= 2 : 5-1 = 4  2:4 VALID ANS = ang

# Quick Quiz :
nm = "Harry"
print(nm[-4:-2])


