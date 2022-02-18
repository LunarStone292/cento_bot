import random

caratteri = '''abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ1234567890!?-%&'''

print("\n inserisci quanto caratteri deve essere lunga la password")

lunghezza = int (input ('''\n caratteri@lunghezza-# '''))

password= ""

for x in range (lunghezza):
    password+= random.choice (caratteri)

print("\n questa è la tua nuova password!: ", password)

