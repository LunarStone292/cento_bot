import os
import platform
import time

if(platform.system() == "Windows"):
    os.system("cls")
if(platform.system() == "Linux"):
    os.system("clear")

print(" linugua inpostata ------> ITALIANO")
print("\n do you want to change language?")
confirm = input("\n (S/n): ")

if(confirm == "S"):
    os.system("python3 cento.py")
if(confirm == "n"):
    if(platform.system() == "Windows"):
        os.system("cls")
    if(platform.system() == "Linux"):
        os.system("clear")
    os.system("python3 language/italiano/italiano.py")

else:
    if(platform.system() == "Windows"):
        os.system("cls")
    if(platform.system() == "Linux"):
        os.system("clear")
    print("\n error")
