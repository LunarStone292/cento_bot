import platform
import os

if(platform.system() == "Windows"):
    os.system("cls")
if(platform.system() == "Linux"):
    os.system("clear")

os.system("python3 language/deutsch/console.py")