import os
from gtts import gTTS
from playsound import playsound

nome = input("\n inserisci qua la tua frase (premi invio per finire):\n\n")

lunghezza_nome = len(nome)
lunghezza_nome_stringa = str(lunghezza_nome)

print("\n la tua frase ha esattamente " + lunghezza_nome_stringa + " lettere (compresi spazzi)")

text = "la tua frase ha esattamente " + lunghezza_nome_stringa + " lettere (compresi spazzi)"
tts = gTTS(text=text, lang='it')
tts.save("voce.mp3")

playsound("voce.mp3")

os.system("del voce.mp3")

os.system("python3 language/italiano/console.py")