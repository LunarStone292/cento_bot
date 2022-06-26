import os
from platform import platform

if(platform.system() == "Windows"):
    os.system("netsh wlan show profiles")
    risposta = input("nome@connessione-# ")
    if(risposta == ""):
        os.system("python3 command/italiano/modem.py")
    else:
        os.system("netsh wlan show profiles " + risposta + " key=clear")
else:
    os.system("ls /etc/NetworkManager/system-connections/")
    risposta = input("nome@connessione-# ")
    if(risposta == ""):
        os.system("python3 command/italiano/modem.py")
    else:
        os.system("cat /etc/NetworkManager/system-connections/" + risposta)
os.system("python3 language/italiano/console.py")
