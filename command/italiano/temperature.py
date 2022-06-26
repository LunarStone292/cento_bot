import webbrowser
import os
import platform

if(platform.system() == "Windows"):
    os.system("cls")
    webbrowser.open('https://weather.com/')
if(platform.system() == "Linux"):
    os.system("clear")
    os.system('firefox https://weather.com/')

os.system("python3 language/italiano/console.py")
