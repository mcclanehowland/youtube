import webbrowser
import time
import os
from pykeyboard import PyKeyboard

k = PyKeyboard()


# url = input("Enter the youtube URL:")
# refresh = input("Enter the refresh time in seconds:")
# browser = input("Enter the browser (e.g chrome/firefox)")
# count = input("How many views do you want?")

url = "https://www.youtube.com/watch?v=jKATcWcbYtA"
refresh = 5
# browser = "chrome"
count = 10




def openURL():
    #  os.system("TASKILL /F /IM" + browser + ".exe")﻿
    webbrowser.open(url)
    time.sleep(int(refresh))
    k.press_key('Control_L')
    k.press_key('W')
    k.release_key('Control_L')
    k.release_key('W')


    for i in range(int(count)):
        print("Webpage has been viewed")
        openURL()

openURL()
