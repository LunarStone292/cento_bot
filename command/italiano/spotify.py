import multiprocessing
import os
import platform
import webbrowser

aggiunta = input("\n vuoi aprire una playlist? (S/n): ")
musica_preferita = input("\n vuoi riprodurre una canzone? (S/N): ")



risposta = "S"
risposta_ = "n"

#playlist
if(aggiunta == "S"):
    scelta = input('\n hai già inserito la playlist precedentemente? (S/n): ')
    if(scelta == "S"):
        f = open("txt/spotify.txt","r") 
        while True:
            line = f.readline() 
            if not line:
                break
            webbrowser.open(line)
        f.close()
    if(scelta == "n"):
        playlist = input("\n inserisci il link dellla playlist: ")
        os.system("echo " + playlist + " > txt/spotify.txt")
        if(platform.system() == "Windows"):
            webbrowser.open(playlist)
        else:
            os.system("firefox " + playlist)

#alternativa
if(aggiunta == risposta_):
    if(musica_preferita == risposta_):
        if(platform.system() == "Windows"):
            webbrowser.open('https://www.spotify.com/')
        else:
            os.system("firefox https://www.spotify.com/")
    if(musica_preferita == risposta):
        canzone = input("inserisci il link della tua canzone preferita")
        if(platform.system() == "Windows"):
            webbrowser.open(canzone)
        else:
            os.system("firefox " + canzone)


os.system("python3 language/italiano/console.py")
