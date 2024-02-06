                    #Map, Filter and Reduce
'''
the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.
'''

# def cube(x):
#     return x**3

# # print(cube(2))

# l = [1,4,6,3,7,5,2]
# newl = []
# for itme in l:
#     newl.append(cube(itme))

# print(newl)

#shortcut
                        #Map 
'''
the map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:

map(function, iterable)

The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.
'''

l = [1,4,6,3,7,5,2]

newl = list(map(lambda x: x**3, l))
print(newl)


                    #Filter

'''
The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:

#filter(predicate, iterable)

The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.
'''

newnewl = list(filter(lambda a: a>4, l))
print(newnewl)


                    #Reduce
'''
The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:

reduce(function, iterable)

The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.

The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.
'''
from functools import reduce

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y: x + y , numbers)

print(sum)