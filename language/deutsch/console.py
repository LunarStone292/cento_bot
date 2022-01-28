from __future__ import annotations
import os
import platform 
import time

#comandi
aiuto = "hilfe"
ora = "std"
temperatura = "welche Temperatur ist es draußen"
timer = "stellen Sie den Timer ein"
pulisci = "klar"
ricerca = "eine Google-Suche durchführen"
ipconfig = "meine ip"
dado = "wirf den Würfel"
uscita = "hinausgehen"
annotazione = "anmerkung"
spotify = "spotify öffnen"
calcolatrice = "benutze den Taschenrechner"
apri_link = "link öffnen"
location = "suchen Sie sich einen Platz"
documento = "offnen Sie ein Textdokument"
moneta = "die Münze werfen"

#input console
console = input("\n cento@help-# ")

#aiuto
if(console == aiuto):
    os.system("python3 command/deutsch/help.py")

#orario
if(console == ora):
    os.system("python3 command/deutsch/time.py")

#temperatura
if(console == temperatura):
    os.system("python3 command/deutsch/temperature.py")

#timer
if(console == timer):
    os.system("python3 command/deutsch/timer.py")

#clear
if(console == pulisci):
    os.system("python3 command/deutsch/clear.py")

#ricerca google
if(console == ricerca):
    os.system("python3 command/deutsch/ricerca.py")

#ip
if(console == ipconfig):
    os.system("python3 command/deutsch/ip.py")

#lancia il dado
if(console == dado):
    print("\n Der Würfel kam heraus: \n")
    os.system("python3 command/deutsch/dado.py")

#uscita
if(console == uscita):
    exit

#annotazione
if(console == annotazione):
    os.system("python3 command/deutsch/note.py")

#apri spotify
if(console == spotify):
    os.system("python3 command/deutsch/spotify.py")

#apri un link
if(console == apri_link):
    os.system("python3 command/deutsch/link.py")

#calcolatrice
if(console == calcolatrice):
    os.system("python3 command/deutsch/calc.py")

#cerca un posto
if(console == location):
    os.system("python3 command/deutsch/location.py")

#apri un documento di testo
if(console == documento):
    os.system("python3 command/deutsch/documento.py")

#lancia la moneta
if(console == moneta):
    os.system("python3 command/deutsch/moneta.py")

