'''
#Exercise 10 Use the NewsAPI and the requests module to 
# fetch the daily news related to different topics. Go to: 
# https://newsapi.org/ and explore the various options to build you application
'''
import requests
import json


query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-01-09&sortBy=publishedAt&apiKey=6dc62bc0de0f48fe935b71a06bf7ade3"

r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------------------------")