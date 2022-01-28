from __future__ import annotations
import os
import time
import platform 
import random

#comandi
aiuto = "aiuto"
ora = "orario"
temperatura = "che temperatura fa fuori"
timer = "imposta timer"
pulisci = "clear"
ricerca = "fai una ricerca su google"
ipconfig = "il mio ip"
dado = "lancia il dado"
uscita = "esci"
annotazione = "annotazione"
spotify = "apri spotify"
calcolatrice = "usa la calcolatrice"
apri_link = "apri un link"
location = "cerca un posto"
documento = "apri un documento di testo"
moneta = "lancia la moneta"
ascii_l = "gioca con le ascii"

#input console
console = input("\n cento@help-# ")

#aiuto
if(console == aiuto):
    os.system("python3 command/italiano/help.py")

#orario
if(console == ora):
    os.system("python3 command/italiano/time.py")

#temperatura
if(console == temperatura):
    os.system("python3 command/italiano/temperature.py")

#timer
if(console == timer):
    os.system("python3 command/italiano/timer.py")

#clear
if(console == pulisci):
    os.system("python3 command/italiano/clear.py")

#ricerca google
if(console == ricerca):
    os.system("python3 command/italiano/ricerca.py")

#ip
if(console == ipconfig):
    os.system("python3 command/italiano/ip.py")

#lancia il dado
if(console == dado):
    print("\n dal dado e' uscito: \n")
    os.system("python3 command/italiano/dado.py")

#uscita
if(console == uscita):
    exit

#annotazione
if(console == annotazione):
    os.system("python3 command/italiano/note.py")

#apri spotify
if(console == spotify):
    os.system("python3 command/italiano/spotify.py")

#apri un link
if(console == apri_link):
    os.system("python3 command/italiano/link.py")

#calcolatrice
if(console == calcolatrice):
    os.system("python3 command/italiano/calc.py")

#cerca un posto
if(console == location):
    os.system("python3 command/italiano/location.py")

#apri un documento di testo
if(console == documento):
    os.system("python3 command/italiano/documento.py")

#lancia la moneta
if(console == moneta):
    os.system("python3 command/italiano/moneta.py")