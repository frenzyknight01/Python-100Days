                                       #Dictionary
'''
Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
'''

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)


'''
Accessing single values:
Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.
'''
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name']) #When key is not in the dictionary it gives error
print(info.get('eligible2')) #When key is not in the dictionary it gives None Only it does not give error



'''
Accessing multiple values:
We can print all the values in the dictionary using values() method.
'''
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())


'''
Accessing keys:
We can print all the keys in the dictionary using keys() method.
'''
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

'''
We can print all the key-value pairs in the dictionary using items() method.
'''
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())

for key in info.keys():
   print(f"The value corresponding to the key {key} is {info[key]}")

for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 