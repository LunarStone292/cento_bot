import os

print("\n inserisci cosa vuoi scrivere\n")
scittura = input(" ")
partizione = input(" inserisci dove salvare il testo: ")

os.system("echo " + scittura + " > " + partizione)

os.system("python3 language/italiano/console.py")