from platform import platform
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
    if(platform.system() == "Windows"):
        webbrowser.open(instagram + account)
    else:
        os.system("firefox " + instagram + account)

if(social == "facebook"):
    if(platform.system() == "Windows"):
        webbrowser.open(facebook + account)
    else:
        os.system("firefox " + facebook + account)

if(social == "tiktok"):
    if(platform.system() == "Windows"):
        webbrowser.open(tiktok + account)
    else:
        os.system("firefox " + tiktok + account)

if(social == "twitch"):
    if(platform.system() == "Windows"):
        webbrowser.open(twitch + account)
    else:
        os.system("firefox " + twitch + account)

if(social == "github"):
    if(platform.system() == "Windows"):
        webbrowser.open(github + account)
    else:
        os.system("firefox " + github + account)

if(social == "youtube"):
    if(platform.system() == "Windows"):
        webbrowser.open(youtube + account)
    else:
        os.system("firefox " + youtube + account)

os.system("python3 language/italiano/console.py")
