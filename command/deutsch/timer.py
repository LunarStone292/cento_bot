import time
import os
import platform

tempo = int(input("\n Wie viele Sekunden soll der Timer dauern?: "))

if(platform.system() == "Windows"):
    os.system("cls")
if(platform.system() == "Linux"):
    os.system("clear")

print(" _____ _                                       _             _       _ ")
print("|_   _(_)_ __ ___   ___ _ __    __ _  ___  ___| |_ __ _ _ __| |_ ___| |_ ")
print("  | | | | '_ ` _ \ / _ \ '__|  / _` |/ _ \/ __| __/ _` | '__| __/ _ \ __| ")
print("  | | | | | | | | |  __/ |    | (_| |  __/\__ \ || (_| | |  | ||  __/ |_ ")
print("  |_| |_|_| |_| |_|\___|_|     \__, |\___||___/\__\__,_|_|   \__\___|\__| ")

time.sleep(tempo)

if(platform.system() == "Windows"):
    os.system("cls")
if(platform.system() == "Linux"):
    os.system("clear")

print(" _____    _ _     _     _ ")
print("|__  /___(_) |_  (_)___| |_   _   _ _ __ ___ ")
print("  / // _ \ | __| | / __| __| | | | | '_ ` _ \ ")
print(" / /|  __/ | |_  | \__ \ |_  | |_| | | | | | | ")
print("/____\___|_|\__| |_|___/\__|  \__,_|_| |_| |_| ")

os.system("cd mp3 & Time-Up.mp3")
os.system("python3 language/deutsch/console.py")