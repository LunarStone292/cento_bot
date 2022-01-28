import os
import platform

if(platform.system() == "Windows"):
    print("\n Öffnen Sie eine der folgenden Anwendungen")
    print("\n Notizen blockieren")
    print("\n word")
    scelta = input("\n cento@help-# ")
    if(scelta == "Notizen blockieren"):
        os.system("start notepad.exe")
    if(scelta == "word"):
        print(" einen Moment...")
        os.system("start WINWORD.exe")
    if(scelta == ""):
        print(" error.")
        os.system("python3 command/italiano/documento.py")

if(platform.system() == "Linux"):
    nome = input("\n geben Sie den Dateinamen ein: ")
    os.system("nano " + nome)

os.system("python3 language/deutsch/console.py")