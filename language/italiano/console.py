from __future__ import annotations
import os
from platform import platform
import time
from turtle import speed
import ctypes
from gtts import gTTS
from playsound import playsound
import telepot
import random
import webbrowser
import getpass


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
logoutt = "torna alla schermata di blocco"
dispositivi = "dispositivi connessi alla rete"
sicurezza = "quanto è sicura la mia password"
lung_fra = "quanti caratteri ha una frase"
del_log = "elimina log"
account = "cerca un account"

#input console
console = input("\n cento@help-# ")

#in caso di errore
if(console != aiuto):
    if(console != ora):
        if(console != orologio):
            if(console != temperatura):
                if(console != timer):
                    if(console != pulisci):
                        if(console != ricerca):
                            if(console != ipconfig):
                                if(console != dado):
                                    if(console != uscita):
                                        if(console != annotazione):
                                            if(console != spotify):
                                                if(console != calcolatrice):
                                                    if(console != apri_link):
                                                        if(console != location):
                                                            if(console != documento):
                                                                if(console != moneta):
                                                                    if(console != spegnimento):
                                                                        if(console != the_pass):
                                                                            if(console != ping):
                                                                                if(console != compiti):
                                                                                    if(console != speedtest):
                                                                                        if(console != mail):
                                                                                            if(console != inf_pc):
                                                                                                if(console != modem):
                                                                                                    if(console != logoutt):
                                                                                                        if(console != dispositivi):
                                                                                                            if(console != sicurezza):
                                                                                                                if(console != lung_fra):
                                                                                                                    if(console != del_log):
                                                                                                                        if(console != account):
                                                                                                                            print("errore.")
                                                                                                                            os.system("python3 language/italiano/console.py")

#aiuto
if(console == aiuto):
    os.system("python3 command/italiano/help.py")

#orario
if(console == ora):
    os.system("python3 command/italiano/time.py")

#orologio
if(console == orologio):
    print("\n premi y per fermare il processo")
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
    os.system("taskkill /IM cmd.exe")

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
    os.system("start vbs/spegnimento.vbs")
    os.system("shutdown /s /t 10")
    text = "spegnimento in corso"
    tts = gTTS(text=text, lang='it')
    tts.save("voce.mp3")
    playsound("voce.mp3")
    os.system("del voce.mp3")

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
    if(platform.system() == "Windows"):
        webbrowser.open("start https://mail.google.com/mail/u/0/")
    else:
        os.system("firefox https://mail.google.com/mail/u/0/")
    os.system("python3 language/italiano/console.py")

#info pc
if(console == inf_pc):
    os.system("python3 command/italiano/inf_pc.py")

#modem
if(console == modem):
    os.system("python3 command/italiano/modem.py")

#sicurezza
if(console == sicurezza):
    os.system("python3 command/italiano/crack-password.py")

#logout
if(console == logoutt):
    ctypes.windll.user32.LockWorkStation()

#dispositivi
if(console == dispositivi):
    os.system("python3 command/italiano/scan.py")

#lunghezza frase
if(console == lung_fra):
    os.system("python3 command/italiano/lunghezza.py")

#del log
if(console == del_log):
    if(platform.system() == "Windows"):
        os.system("del txt/log.txt")
        os.system("del txt/spotify.txt")
        os.system("type nul > txt/log.txt")
        os.system("type nul > txt/spotify.txt")
    else:
        os.system("rm -r txt/log.txt")
        os.system("rm -r txt/spotify.txt")
        os.system("echo > txt/log.txt")
        os.sysytem("echo > txt/spotify.txt")
    print("riavviando bot...")
    time.sleep(1)
    print("riavviando bot..")
    time.sleep(1)
    print("riavviando bot.")
    time.sleep(1)
    print("riavviando bot..")
    time.sleep(1)
    print("riavviando bot...")
    time.sleep(2)
    os.system("python3 cento.py")

#cerca account
if(console == account):
    os.system("python3 command/italiano/account.py")

