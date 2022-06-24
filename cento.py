import os
import platform
import getpass

if(platform.system() == "Linux"):
            print("\n this bot is not supported for linux \n\n")
            exit

f = open("txt/log.txt","r") 
while True:
    line = f.readline() 
    if(line == ""):
        os.system("cls")
        print("              _")
        print("__      _____| | ___ ___  _ __ ___   ___ ")
        print("\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ ")
        print(" \ V  V /  __/ | (_| (_) | | | | | |  __/ ")
        print("  \_/\_/ \___|_|\___\___/|_| |_| |_|\___| ")

        print("\n\n Hi " + getpass.getuser() + ", i'm cento and i'm happy to help you")
        print("\n ---------------------------------------------")
        print("\n italiano")
        print("\n ---------------------------------------------")
        language = input("\n please, enter a language : ")

        if(language == "italiano"):
            os.system("echo 1 > txt/log.txt")
            os.system("python3 language/italiano/verifica.py")
        else:
            print("errore")
            os.system("python3 cento.py")
    else:
        os.system("python3 language/italiano/console.py")
f.close()
