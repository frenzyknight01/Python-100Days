'''
                    Requests module
The Python Requests module is an HTTP library that enables
 developers to send HTTP requests in Python. This module 
 enables you to send HTTP requests using Python code and 
 makes it possible to interact with APIs and web services.
'''

'''
Get Request
Once you have installed the Requests module, you can start
 using it to send HTTP requests. Here is a simple example 
 that sends a GET request to the devtown homepage:
'''
# import requests
# response = requests.get("https://www.devtown.in")
# print(response.text)

'''
                    Post Request
Here is another example that sends a POST request to a web service and includes a custom header:
'''
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
  "title": 'Unknown',
  "body": 'night',
  "userId": 1,
}

headers = {
    'Content-type': 'application/json; charset=UTF-8',
}

response = requests.post(url, headers=headers, json=data)

print(response.text)

'''
                        bs4 Module
There is another module called BeautifulSoup which is used for web scraping in Python. I have personally used bs4 module to finish a lot of freelancing task.
'''

#It gives only h2 tags whatever you want. they give it.
from bs4 import BeautifulSoup
import requests

url = "https://devtown.in"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


for heading in soup.find_all("h2"):
    print(heading.text)

