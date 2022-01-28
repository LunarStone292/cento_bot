import os
import webbrowser

sito = input("\n geben Sie den Link ein: ")

sito_false = ""

if(sito != sito_false):
    webbrowser.open(sito)

else:
    print("\n ungültiger Befehl")

os.system("python3 language/deutsch/console.py")