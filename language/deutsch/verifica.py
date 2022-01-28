import os
import platform
import time

if(platform.system() == "Windows"):
    os.system("cls")
if(platform.system() == "Linux"):
    os.system("clear")

print(" Sprache eingestellt ------> DEUTSCH")
print("\n do you want to change language?")
confirm = input("\n (J/n): ")

if(confirm == "J"):
    os.system("python3 cento.py")
if(confirm == "n"):
    if(platform.system() == "Windows"):
        os.system("cls")
    if(platform.system() == "Linux"):
        os.system("clear")
    os.system("python3 language/deutsch/deutsch.py")

else:
    if(platform.system() == "Windows"):
        os.system("cls")
    if(platform.system() == "Linux"):
        os.system("clear")
    print("\n error")
