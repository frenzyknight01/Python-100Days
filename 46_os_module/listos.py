import os 
folders = os.listdir("data")

# print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))


print(os.getcwd()) #We can check our location path 

#os.chdir("/Users") #we can change directory

#os.remove("data")  #remove directory
#os.rmdir("data")  #remove directory
