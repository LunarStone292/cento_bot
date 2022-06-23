from __future__ import annotations
import os
import time
from turtle import speed

#comandi
aiuto = "help"
ora = "time"
orologio = "clock"
temperatura = "what is the temperature outside"
timer = "set timer"
pulisci = "clear"
ricerca = "do a google search"
ipconfig = "my ip"
dado = "roll the dice"
uscita = "exit"
annotazione = "annotation"
spotify = "open spotify"
calcolatrice = "use the calculator"
apri_link = "open a link"
location = "look for a place"
documento = "open a text document"
moneta = "flip the coin"
spegnimento = "turn off your pc"
the_pass = "I need a new password"
ping = "check if a host is online"
compiti = "help me with homework"
speedtest = "fai uno speedtest"
mail = "open gmail"
inf_pc = "information on my pc"
modem = "data on my modem"


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
