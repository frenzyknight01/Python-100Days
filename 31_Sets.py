                                        #Sets
'''Sets are unordered collection of data items.They store multiple items in a single variable.
Set items are separated by commas and enclosed within curly brackets {}.
Sets are unchangeable, meaning you cannot change items of the set once created.
Sets do not contain duplicate items.
'''

sett = {10,2,15,2,5,"Yellow"} #set
print(sett)

#Empty set
Harry = set() #it can give empty sets
# Harry = {} #IT can give empty dictionary 
print(type(Harry))

for info in sett:
    print(info)