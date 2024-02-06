                            #Tuple are immutable we can not change it.
tpl = (3,6,9,"Green","Yellow")
print(type(tpl))
print(tpl)
                            #Tuple[start : end : jumpIndex]
print(len(tpl))
print(tpl[0])
print(tpl[-1]) #Negative Indexing
print(tpl[2]) #Positive Indexing

if 9 in tpl:
    print("Yes 9 is present in tuple")
else:
    print("9 is Absent in tuple.")

tpl2 = tpl[0:5] #We can also create tuple from existing tuple
print(tpl2)

["Hello",2334,"dshg"] #list
("afdh","ssdgh",35) #tuple
{"Hello","asjhfsdh",6565, "name =meet"} #dictionary