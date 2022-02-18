from __future__ import annotations
import os
import time
from turtle import speed

#comandi
aiuto = "aiuto"
ora = "orario"
orologio = "orologio"
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
spegnimento = "spegni il pc"
the_pass = "mi serve una nuova password"
ping = "controlla se un host è online"
compiti = "aiutami con i compiti"
speedtest = "fai uno speedtest"
mail = "apri gmail"
inf_pc = "informazioni sul mio pc"
modem = "dati sul mio modem"


#input console
console = input("\n cento@help-# ")

#aiuto
if(console == aiuto):
    os.system("python3 command/italiano/help.py")

#orario
if(console == ora):
    os.system("python3 command/italiano/time.py")

#orologio
if(console == orologio):
    print("\n premi Ctrl+c per fermare il processo")
    time.sleep(3)
    os.system("python3 command/italiano/orologio.py")

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

#spegni il pc
if(console == spegnimento):
    os.system("shutdown /s /t 00")

#nuova password
if(console == the_pass):
    os.system("python3 command/italiano/pass.py")

#ping
if(console == ping):
    print("\n se si deve mettere l'url non mettere l'http o l'https")
    host = input("\n inserisci l'ip o l'URL: ")
    os.system("ping " + host)

#compiti
if(console == compiti):
    os.system("python3 command/italiano/compiti/tipo.py")

#speedtest
if(console == speedtest):
    os.system("python3 command/italiano/speedtest-cli/speedtest.py")

#gmail
if(console == mail):
    os.system("start https://mail.google.com/mail/u/0/")
    os.system("python3 language/italiano/console.py")

#info pc
if(console == inf_pc):
    os.system("python3 command/italiano/inf_pc.py")

#modem
if(console == modem):
    os.system("python3 command/italiano/modem.py")