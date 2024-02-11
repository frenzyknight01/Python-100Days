'''
            Exercise 11 - Drink Water Reminder
Write a python program which reminds you of drinking water
every hour or two. Your program can either beep or send 
desktop notifications for a specific operating system
'''

import time
import os
from win10toast import ToastNotifier

def get_time_input():
    hour = int(input("Enter hours of interval: "))
    minutes = int(input("Enter minutes of interval: "))
    seconds = int(input("Enter seconds of interval: "))
    time_interval = seconds + (minutes * 60) + (hour * 3600)
    return time_interval

def notify_windows():
    notification = ToastNotifier()
    notification.show_toast("Time to drink water", "Stay hydrated!", duration=5)

def notify_macos():
    os.system('osascript -e \'display notification "Time to drink water" with title "Stay hydrated!"\'')

def notify_linux():
    os.system('notify-send "Time to drink water" "Stay hydrated!"')

def start_time(time_interval):
    while True:
        time.sleep(time_interval)
        notify_windows()
        notify_macos()
        notify_linux()

if __name__ == '__main__':
    time_interval = get_time_input()
    start_time(time_interval)
