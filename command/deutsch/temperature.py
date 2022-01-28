import webbrowser
import os
import platform

if(platform.system() == "Windows"):
    os.system("cls")
if(platform.system() == "Linux"):
    os.system("clear")
webbrowser.open('https://weather.com/')

os.system("python3 language/deutsch/console.py")