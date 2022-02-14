import multiprocessing
import os
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
        webbrowser.open(playlist)

#alternativa
if(aggiunta == risposta_):
    if(musica_preferita == risposta_):
        webbrowser.open('https://www.spotify.com/')
    if(musica_preferita == risposta):
        canzone = input("inserisci il link della tua canzone preferita")
        webbrowser.open(canzone)


os.system("python3 language/italiano/console.py")