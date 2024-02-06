'''
                The time Module
The time module in Python provides a set of functions to 
work with time-related operations, such as timekeeping, 
formatting, and time conversions. This module is part of 
the Python Standard Library and is available in all Python
installations, making it a convenient and essential tool
 for a wide range of applications. In this day 84
  tutorial, we'll explore the time module in Python and 
  see how it can be used in different scenarios.

'''

'''
                    time.time()
The time.time() function returns the current time as a
 floating-point number, representing the number of seconds 
 since the epoch (the point in time when the time module 
 was initialized). The returned value is based on the 
 computer's system clock and is affected by time 
 adjustments made by the operating system, such as 
 daylight saving time. 
'''

import time

def usingWhile():
    i = 0
    while i<5000:
        i = i + 1
        print(i)

def usingFor():
    for i in range(5000):
        print(i+1)

init = time.time()
usingFor()
t1 = (time.time() - init)

init = time.time()
usingWhile()
print(time.time() - init)
print(t1)

'''
                    time.sleep()
The time.sleep() function suspends the execution of the
current thread for a specified number of seconds. This
function can be used to pause the program for a certain
period of time, allowing other parts of the program to 
run, or to synchronize the execution of multiple 
threads.
'''
import time
print(4)
time.sleep(10)
print("This is printed after 3 seconds")

'''
                    time.strftime()
The time.strftime() function formats a time value as a
string, based on a specified format. This function is
particularly useful for formatting dates and times in a
human-readable format, such as for display in a GUI, a
log file, or a report.
'''
import time

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_time)
