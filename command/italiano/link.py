import os
from platform import platform
import webbrowser

sito = input("\n inserisci il link: ")

sito_false = ""

if(sito != sito_false):
    if(platform.system() == "Windows"):
        webbrowser.open(sito)
    else:
        os.system("firefox " + sito)

else:
    print("\n comando invalido")

os.system("python3 language/italiano/console.py")
