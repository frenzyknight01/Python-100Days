                        #File IO
'''
Opening a File
Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.
'''


'''
Modes in file
There are various modes in which we can open files.

read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

create (x): This mode creates a file and gives an error if the file already exists.

text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

binary (b): used to handle binary files (images, pdfs, etc).
'''

                        #Reading a file
f = open('49_myfile.txt', 'r')
# print(f)
contents = f.read()
print(contents)

                        #Writing to a File
'''
Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.
'''
f = open('49_myfile.txt','w')
f.write("Hello, world!")

f = open('49_myfile.txt','a') 
f.write("Hello, world!")

                        #Closing a file
'''
It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.

To close a file, you can use the close() method.
'''
f = open('49_myfile.txt','r')
f.read()
f.close

                    #For closing file second option
'''
The 'with' statement
Alternatively, you can use the with statement to automatically close the file after you are done with it.
'''

with open('49_myfile.txt','a') as f:
    f.write("Hey I am inside with")