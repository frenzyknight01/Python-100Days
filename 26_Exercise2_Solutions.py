                            #Exercise 2 solution 
import time
t = print(time.strftime("%H:%M:%S"))
hour = int(time.strftime("%H"))
# input("Enter hour: ")
print(hour)

if (hour>=0 and hour<12):
    print("Good Morning sir!")
elif (hour>=12 and hour<17):
    print("Good Afternoon sir!")
elif (hour>=17 and hour<=0):
    print("Good Night sir!") 