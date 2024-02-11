'''
                            Async IO
Asynchronous I/O, or async for short, is a programming 
pattern that allows for high-performance I/O operations in 
a concurrent and non-blocking manner. In Python, async 
programming is achieved through the use of the asyncio 
module and asynchronous functions.
'''


import time
import asyncio
import requests

                        #First Program
# async def function1():
#     await asyncio.sleep(1)
#     print("func 1")
    
# async def function2():
#     await asyncio.sleep(1)
#     print("func 2")

# async def function3():
#     await asyncio.sleep(3)
#     print("func 3")


# async def main():
#     task = asyncio.create_task(function1())
#     # await function1()
#     await function2()
#     await function3()

# asyncio.run(main())

                        #Second Program
async def function1():
    print("func 1")
    URL = "https://unsplash.com/photos/a-very-tall-mountain-with-a-lot-of-snow-on-it-_X2pRyHkGQs"
    response = requests.get(URL)
    open("1.jpg", "wb").write(response.content)
    
async def function2():
    print("func 2")
    URL = "https://unsplash.com/photos/a-church-with-a-lot-of-snow-on-top-of-it-qJOFxKtOvjY"
    response = requests.get(URL)
    open("2.jpg", "wb").write(response.content)

async def function3():
    print("func 3")
    URL = "https://unsplash.com/photos/a-crowd-of-people-walking-down-a-street-next-to-tall-buildings-68CopG3fmrg"
    response = requests.get(URL)
    open("3.jpg", "wb").write(response.content)

async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)

asyncio.run(main())

                                  #Third Program
async def function1():
  print("func 1") 
  URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
  response = requests.get(URL)
  open("instagram.jpg", "wb").write(response.content)
   
  return "Harry"
  
async def function2():
  print("func 2") 
  URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram2.jpg", "wb").write(response.content)
  
async def function3():
  print("func 3")
  URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram3.jpg", "wb").write(response.content)

async def main():
  await function1()
  await function2()
  await function3()
  print(L)

asyncio.run(main())