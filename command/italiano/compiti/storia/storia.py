import imp


import os
import webbrowser

sito = input("\n inserisci il nome dell'argomento: ")
webbrowser.open('https://it.wikipedia.org/wiki/' + sito)

os.system("python3 language/italiano/console.py")