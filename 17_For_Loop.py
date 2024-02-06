                                                    #For loop
name = "Abhishek"
for i in name: #It create for loop.
    print(i)
    if i =='b':
        print("This is something special!")

colors = ['Red', 'Yellow', 'Green', 'Blue']
for color in colors:
    print(color)
    for i in color:
        print(i)

# for k in range(5): #Range have three parameters (start, stop, step) 
#     print(k) #range gives (0 to 4 not including 5)

for k in range(0,9):
    print(k + 1) # when we use + 1 range gives (All including numbers)

# for k in range(1,20001):
#     print(k)

# for k in range(1, 9, 2):
#     print(k)