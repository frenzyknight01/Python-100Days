import win32com.client
 
shoutout = ["Rohan","Ravi","Rutvik","Ronak"]

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for name in shoutout:
    s = name
    speaker.Speak(f"Hello {name}")


