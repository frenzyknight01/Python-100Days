'''
                        Multithreading
Multithreading is a technique in programming that allows 
multiple threads of execution to run concurrently within a 
single process. In Python, we can use the threading module 
to implement multithreading. In this tutorial, we will 
take a closer look at the threading module and its various 
functions and how they can be used in Python.

                        Importing Threading
We can use threading by importing the threading module.

import threading


                        Functions
The following are some of the most commonly used functions in the threading module:

threading.Thread(target, args): This function creates a new thread that runs the target function with the specified arguments.

threading.Lock(): This function creates a lock that can be used to synchronize access to shared resources between threads.
'''

import threading
import time
from concurrent.futures import ThreadPoolExecutor  #ThreadPoolingExecuter

def func(seconds):
    print(f"Sleeping for {seconds}")
    time.sleep(seconds)
    return seconds

def main():

    time1 = time.perf_counter()
    # #Normal code
    # func(4)
    # func(2)
    # func(1)
    # time2 = time.perf_counter()
    # print(time2 - time1)


    #same code using Threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    time2 = time.perf_counter()
    print(time2 - time1)

                        #ThreadPoolingExecuter
from concurrent.futures import ThreadPoolExecutor
def PoolingDemo():
    with ThreadPoolExecutor() as executer:
                    #First Method
        future1 = executer.submit(func, 4)
        future2 = executer.submit(func, 2)
        future3 = executer.submit(func, 5)
        print(future1.result())
        print(future2.result())
        print(future3.result())

                    #Second method
        # l = [3,5,2,4]
        # results = executer.map(func, l)
        # for result in results:
        #     print(result)

PoolingDemo()

