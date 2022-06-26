import time
import os
import platform

tempo = int(input("\n quanti secondi deve durere il timer?: "))

if(platform.system() == "Windows"):
    os.system("cls")
if(platform.system() == "Linux"):
    os.system("clear")

print(" _   _                                        _   _ _ ")
print("| |_(_)_ __ ___   ___ _ __   _ __   __ _ _ __| |_(_) |_ ___ ")
print("| __| | '_ ` _ \ / _ \ '__| | '_ \ / _` | '__| __| | __/ _ \ ")
print("| |_| | | | | | |  __/ |    | |_) | (_| | |  | |_| | || (_) | ")
print(" \__|_|_| |_| |_|\___|_|    | .__/ \__,_|_|   \__|_|\__\___/ ")
print("                            |_| ")

time.sleep(tempo)

if(platform.system() == "Windows"):
    os.system("cls")
if(platform.system() == "Linux"):
    os.system("clear")

print(" _   _                              _")
print("| |_(_)_ __ ___   ___    ___  _   _| |_")
print("| __| | '_ ` _ \ / _ \  / _ \| | | | __|")
print("| |_| | | | | | |  __/ | (_) | |_| | |_")
print(" \__|_|_| |_| |_|\___|  \___/ \__,_|\__|")

if(platform.system() == "Windows"):
    os.system("cd mp3 & Time-Up.mp3")
else:
    os.system("cd mp3 && xdg-open Time-Up.mp3 && cd ..")
os.system("python3 language/italiano/console.py")
