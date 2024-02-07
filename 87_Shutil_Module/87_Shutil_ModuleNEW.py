'''
                        Shutil Module
Shutil is a Python module that provides a higher level 
interface for working with file and directories. The name 
"shutil" is short for shell utility. It provides a 
convenient and efficient way to automate tasks that are 
commonly performed on files and directories. In this repl, 
we'll take a closer look at the shutil module and its 
various functions and how they can be used in Python.


                Importing shutil
The syntax for importing the shutil module is as follows:

import shutil

                        Functions
The following are some of the most commonly used functions in the shutil module:

shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. If the destination location already exists, the original file will be overwritten.

shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.

shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.
'''

import shutil

# #Create New file and save same content to new file
# shutil.copy("87_Shutil_Module.py","87_Shutil_ModuleNEW.py") 

# #Create New file and save  same content to new file but it also preserves more metadata about the original file, such as the timestamp.
# shutil.copy2("87_Shutil_Module.py","87_Shutil_ModuleNEW.py")

# # Copying a directory
# shutil.copytree("tutorial","mytutorial")

# # Moving a file & folder
# shutil.move("mytutorial","tutorial")

import os
os.remove("tutorial\file.file")