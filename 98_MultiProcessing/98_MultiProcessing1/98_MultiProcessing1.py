'''
                      Multiprocessing
Multiprocessing is a Python module that provides a simple 
way to run multiple processes in parallel. It allows you 
to take advantage of multiple cores or processors on your 
system and can significantly improve the performance of 
your code. In this repl, we'll take a closer look at the 
multiprocessing module and its various functions and how 
they can be used in Python.

                Importing Multiprocessing 
We can use multiprocessing by importing the multiprocessing module.

import multiprocessing


Now, to use multiprocessing we need to create a process 
object which calls a start() method. The start() method 
runs the process and then to stop the execution, we use 
the join() method. Here's how we can create a simple 
process.
'''
import multiprocessing
import requests

                           #Normal code
# def DownloadFile(url, name):
#   print(f"Started Downloading {name}")
#   response = requests.get(url)
#   open(f"98_MultiProcessing1/NormalCodeExe/file{name}.jpg","wb").write(response.content)
#   print(f"Finished Downloading {name}")

# if __name__ == "__main__":    
#   url = "https://picsum.photos/2000/3000"
#   pros = []
#   for i in range(5):
#     DownloadFile(url, i)


                    #Using Multiprocessing
def DownloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"98_MultiProcessing1/MultiProcessingExe/file{name}.jpg","wb").write(response.content)
  print(f"Finished Downloading {name}")

  
if __name__ == "__main__":    
  url = "https://picsum.photos/2000/3000"
  pros = []
  for i in range(5):
    p = multiprocessing.Process(target=DownloadFile, args=[url,i])
    p.start()
    pros.append(p)

  for p in pros:
    p.join()