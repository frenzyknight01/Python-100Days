                    #Exercise-4 
'''
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end
  now append three random characters at the starting and the end
else:
  simply reverse the string

Decoding:
if the word contains less than 3 characters, reverse it
else:
  remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

Your program should ask whether you want to code or decode
'''

import random

welcome = "Welcome to the Encryption - Decryption"
print(welcome.center(75,"."))

x = int(input("Please Choose Option From this\n1.Encode\n2.Decode\n0.Exit\n: "))

def encode():
    code = str(input("Enter Input a string of text to encode: "))
    if len(code) == 2:
        return code[::-1]

    elif len(code) >= 3:
        first_letter = code[0]
        code = code[1:] + first_letter
        random_chars1 = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=3))
        random_chars2 = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=3))
        return random_chars1 + code + random_chars2
    else:
        print("Please Enter strings")


def decode():
    code = str(input("Enter Input a string of text to decode: "))
    if len(code) == 2:
        return code[::-1]

    elif len(code) >= 3:
        # random_chars = code[:3] + code[:-3]
        code = code[3:-3]
        return code[-1] + code[:-1]

    else:
        print("Please Enter strings")


match x:
    case 1:
        print(encode())

    case 2:
        print(decode())

    case 0:
        exit

    case _:
        print("Invalid characters Please Enter only string")
    

    



