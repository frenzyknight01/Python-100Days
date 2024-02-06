import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H') #%H means current Hours
print(timestamp)
timestamp = time.strftime('%M') #%M means current Minutes
print(timestamp) 
timestamp = time.strftime('%S') #%S means current seconds
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

print(time.strftime("%a, %d %b %Y, %H:%M:%S")) #%a means day name, %d means month day(0-31), %b means month name, %H means current hour, %M means current minutes, %S means current second