'''
        Exercise 11 - Drink Water Reminder (Solution)
Write a python program which reminds you of drinking water 
every hour or two. Your program can either beep or send 
desktop notifications for a specific operating system

'''


import time
from plyer import notification

Repeat_Interval = 15

while True:
    notification_title = "Drink Water Reminder"
    notification_message = "Hey Unknown, Drink water!"
    notification.timeout = 5

    notification.notify(
        title = notification_title,
        message = notification_message,
    )

    time.sleep(Repeat_Interval)