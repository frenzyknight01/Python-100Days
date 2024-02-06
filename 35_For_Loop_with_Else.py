                    #For Loop with else 
'''
Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.
'''

for i in range(6):
    print(i)

else:
    print("sorry no i")



for i in range(6):
    print(i)
    if i == 4: #At that time else not execute cuz loop was completed
        break

else:
    print("sorry no i")

    

                        #While loop with else
i = 0
while i<6:
    print(i)
    i = i + 1

else:
    print("Sorry no i")


i = 0
while i<6:
    print(i)
    i = i + 1
    if i == 4:#At that time else not execute cuz loop was completed
        break

else:
    print("Sorry no i")