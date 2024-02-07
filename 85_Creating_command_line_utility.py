'''
            Creating Command Line Utilities
Command line utilities are programs that can be run from 
the terminal or command line interface, and they are an 
essential part of many development workflows. In Python, 
you can create your own command line utilities using the 
built-in argparse module.

Syntax
Here is the basic syntax for creating a command line utility using argparse in Python:
'''
'''
            #Adding optinal arguments
import argparse 

parse = argparse.ArgumentParser()

parse.add_argument("-o", "--optional",help = "description of optional argument",default="default_value")

args = parse.parse_args()

print(args.optional)
 

                #Adding positional arguments
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("positional", help="description of positional argument")

args = parser.parse_args()

print(args.positional)

                #Adding arguments with type
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", type=int, help="description of integer argument")

args = parser.parse_args()

print(args.n)
'''

import argparse
import requests

def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    f.write(chunk)
        return local_filename


parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file")
parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)


'''
Conclusion
Creating command line utilities in Python is a 
straightforward and flexible process thanks to the 
argparse module. With a few lines of code, you can create 
powerful and customizable command line tools that can make 
your development workflow easier and more efficient. 
Whether you're working on small scripts or large 
applications, the argparse module is a must-have tool for 
any Python developer.
'''