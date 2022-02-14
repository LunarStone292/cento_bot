import os
import platform

if(platform.system() == "Windows"):
    print("\n apri una delle seguinti applicazioni")
    print("\n blocco note")
    print("\n word")
    scelta = input("\n cento@help-# ")
    if(scelta == "blocco note"):
        os.system("start notepad.exe")
    if(scelta == "word"):
        print(" un momento...")
        os.system("start WINWORD.exe")
    if(scelta == ""):
        print(" error.")
        os.system("python3 command/italiano/documento.py")

if(platform.system() == "Linux"):
    nome = input("\n inserisci il nome del file: ")
    os.system("nano " + nome)

os.system("python3 language/italiano/console.py")