from gtts import gTTS
from playsound import playsound
import os
import platform
import time

if(platform.system() == "Windows"):
    os.system("cls")
if(platform.system() == "Linux"):
    os.system("clear")

print(" linugua impostata ------> ITALIANO")
print("\n do you want to change language?")

text = "lingua impostata, italiano"

tts = gTTS(text=text, lang='it')
tts.save("voce.mp3")

playsound("voce.mp3")

os.system("del voce.mp3")

confirm = input("\n (S/n): ")


if(confirm == "S"):
    os.system("cls")
    os.system("del txt/log.txt")
    os.system("type nul > txt/log.txt")
    os.system("python3 cento.py")
if(confirm == "n"):
    os.system("cls")
    os.system("python3 language/italiano/italiano.py")
else:
    os.system("cls")
    print("\n error")
