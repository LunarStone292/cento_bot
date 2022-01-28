import os

print("\n Welche Arten von Operationen möchten Sie verwenden?")
print("\n 1. Addition")
print("\n 2. Subtraktion")
print("\n 3. Teilung")
print("\n 4. Multiplikation")

operazione = int(input("\n geben Sie ein, was Sie tun möchten: "))

if(operazione == 1):
    addendo_1 = int(input("\n Geben Sie die Nummer ein: "))
    addendo_2 = int(input("\n Geben Sie die Nummer ein_2: "))
    print("\n Das Ergebnis ist: ", addendo_1 + addendo_2)
if(operazione == 2):
    minuendo = int(input("\n Geben Sie die Nummer ein: "))
    sottraendo = int(input("\n Geben Sie die Nummer ein_2: "))
    print("\n Das Ergebnis ist: ", minuendo-sottraendo)
if(operazione == 3):
    dividendo = int(input("\n Geben Sie die Nummer ein: "))
    divisore = int(input("\n Geben Sie die Nummer ein_2: "))
    print("\n Das Ergebnis ist: ", dividendo/divisore )
if(operazione == 4):
    fattore_1 = int(input("\n Geben Sie die Nummer ein: "))
    fattore_2 = int(input("\n Geben Sie die Nummer ein_2: "))
    print("\n Das Ergebnis ist: ", fattore_1*fattore_2)

os.system("python3 language/italiano/console.py")