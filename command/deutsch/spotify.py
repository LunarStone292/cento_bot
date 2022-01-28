import multiprocessing
import os
import webbrowser

aggiunta = input("\n Möchten Sie eine Wiedergabeliste öffnen? (J/n): ")
musica_preferita = input("\n Willst du ein Lied spielen? (J/n): ")



risposta = "J"
risposta_ = "n"

#playlist
if(aggiunta == risposta):
    scelta = input('\n hast du die playlist schon vorher eingegeben? (J/n): ')
    if(scelta == risposta):
        f = open("txt/spotify.txt","r") 
        while True:
            line = f.readline() 
            if not line:
                break
            webbrowser.open(line)
        f.close()
    if(scelta == risposta_):
        playlist = input("\n Geben Sie den Playlist-Link ein: ")
        os.system("echo " + playlist + " > txt/spotify.txt")
        webbrowser.open(playlist)

#alternativa
if(aggiunta == risposta_):
    if(musica_preferita == risposta_):
        webbrowser.open('https://www.spotify.com/')
    if(musica_preferita == risposta):
        canzone = input(" Geben Sie den Link des Songs ein: ")
        webbrowser.open(canzone)


os.system("python3 language/deutsch/console.py")