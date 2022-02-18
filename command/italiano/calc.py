import os

print("\n quali tipi di operazione vuoi usare?")
print("\n 1. addizione")
print("\n 2. sottrzaione")
print("\n 3. divisione")
print("\n 4. moltiplicazione")

operazione = int(input("\n inserisci cosa vuoi fare: "))

if(operazione == 1):
    addendo_1 = int(input("\n inserisci l'addendo: "))
    addendo_2 = int(input("\n inserisci l'addendo 2: "))
    risposta = addendo_1 + addendo_2
    print("\n il risultato e': ", risposta)
if(operazione == 2):
    minuendo = int(input("\n inserisci il minuendo: "))
    sottraendo = int(input("\n inserisci il sottraendo: "))
    risposta_2 = minuendo - sottraendo
    print("\n il risultato e': ", risposta_2)
if(operazione == 3):
    dividendo = int(input("\n inserisci il dividendo: "))
    divisore = int(input("\n inserisci il divisore: "))
    risposta_3 = dividendo/divisore
    print("\n il risultato e': ", risposta_3)
if(operazione == 4):
    fattore_1 = int(input("\n inserisci il fattore: "))
    fattore_2 = int(input("\n inserisci il fattore 2: "))
    risposta_4 = fattore_1*fattore_2
    print("\n il risultato e': ", risposta_4)
os.system("python3 language/italiano/console.py")