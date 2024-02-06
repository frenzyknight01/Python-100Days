                    #seek() and tell() functions
'''
In Python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes, and in-memory buffers.
'''

'''
seek() function
The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. For example:
'''

with open("51_sample.txt",'r') as f:
    f.seek(10) #It give your specific position in byte 

    data = f.read(3)
    print(data)


'''
tell() function
The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position. For example:
'''

# with open("51_sample.txt",'r') as f:
#     f.seek(10) # Seek to the saved position

#     print(f.tell())#It gives your save current position
#     data = f.read(3) # Read the first 10 bytes
#     print(data)

    
'''
truncate() function
When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.

Here is an example of how to use the truncate function:
'''

# with open('51_sample.txt','w') as f:
#     f.write('Hello World!')
#     f.truncate(5)


# with open('51_sample.txt','r') as f:
#     print(f.read())