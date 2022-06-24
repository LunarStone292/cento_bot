import webbrowser
import os

tiktok = "https://tiktok.com/@"
instagram = "https://www.instagram.com/"
facebook = "https://www.facebook.com/"
twitch = "https://www.twitch.tv/"
github = "https://github.com/"
youtube = "https://www.youtube.com/c/"

account = input("\n inserisci il nome dell'account: ")

print('''\n questi sono i social: 
 instagram
 facebook
 tiktok
 twitch
 github
 youtube''')

social = input("\n inserisci il nome del social: ")

if(social == "instagram"):
    webbrowser.open(instagram + account)

if(social == "facebook"):
    webbrowser.open(facebook + account)

if(social == "tiktok"):
    webbrowser.open(tiktok + account)

if(social == "twitch"):
    webbrowser.open(twitch + account)

if(social == "github"):
    webbrowser.open(github + account)

if(social == "youtube"):
    webbrowser.open(youtube + account)

os.system("python3 language/italiano/console.py")