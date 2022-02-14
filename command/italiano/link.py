import os
import webbrowser

sito = input("\n inserisci il link: ")

sito_false = ""

if(sito != sito_false):
    webbrowser.open(sito)

else:
    print("\n comando invalido")

os.system("python3 language/italiano/console.py")