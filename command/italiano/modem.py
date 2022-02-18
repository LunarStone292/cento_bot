import os

os.system("netsh wlan show profiles")

risposta = input("nome@connessione-# ")

if(risposta == ""):
    os.system("python3 command/italiano/modem.py")
else:
    os.system("netsh wlan show profiles " + risposta + " key=clear")

os.system("python3 language/italiano/console.py")