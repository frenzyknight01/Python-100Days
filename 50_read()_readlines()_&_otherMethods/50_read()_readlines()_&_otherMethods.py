                        #readlines() method
'''
The readline() method reads a single line from the file.
If we want to read multiple lines, we can use a loop.

The readlines() method reads all the lines of the file and 
returns them as a list of strings.
'''


# f = open('50_myfile2.txt','r')
# i = 0
# while True:
#     i += 1
#     line = f.readline()
#     if not line: 
#         break     
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student {i} in IDT is : {m1}")
#     print(f"Marks of student {i} in CGM is : {m2}")
#     print(f"Marks of student {i} in WT is : {m3}")
    
#     print(line)


                        #writelines() method
'''
The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.
'''

# f = open('50_myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()