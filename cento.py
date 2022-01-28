import os
import platform
import getpass

#windows

if(platform.system() == "Windows"):
    os.system("cls")
    print("              _")
    print("__      _____| | ___ ___  _ __ ___   ___ ")
    print("\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ ")
    print(" \ V  V /  __/ | (_| (_) | | | | | |  __/ ")
    print("  \_/\_/ \___|_|\___\___/|_| |_| |_|\___| ")
if(platform.system() == "Linux"):
    os.system("clear")
    os.system("figlet welcome")

print("\n\n Hi " + getpass.getuser() + ", i'm cento and i'm happy to help you")
print("\n ---------------------------------------------")
print("\n italiano")
print("\n english")
print("\n deutsch")
print("\n ---------------------------------------------")
language = input("\n please, enter a language : ")

if(language == "italiano"):
    os.system("python3 language/italiano/verifica.py")
if(language == "english"):
    os.system("python3 language/english/verifica.py")
if(language == "deutsch"):
    os.system("python3 language/deutsch/verifica.py")