import os
from gtts import gTTS
from playsound import playsound
import os

#inizio codice
print(" ciao io sono cento e sono felice di aiutarti")
print("\n chiedimi qualcosa se no scrivi (aiuto)")

text = "ciao, io sono cento e sono felice di aiutarti, chiedimi qualcosa se no scrivi aiuto"

tts = gTTS(text=text, lang='it')
tts.save("voce.mp3")

playsound("voce.mp3")

os.system("del voce.mp3")

os.system("python3 language/italiano/console.py")
