import os

print("\n geben Sie ein, was Sie schreiben möchten\n")
scittura = input(" ")
partizione = input(" Geben Sie an, wo der Text gespeichert werden soll: ")

os.system("echo " + scittura + " > " + partizione)

os.system("python3 language/deutsch/console.py")