import os

print("\n che tipo di materia devi svolgere:")
print(''' matematica
 storia
 lingua straniera''')

scelta = input("\n scegli la materia: ")
if(scelta == "lingua straniera"):
    os.system("python3 command/italiano/compiti/inglese/translate.py")

if(scelta == "storia"):
    os.system("python3 command/italiano/compiti/storia/storia.py")

if(scelta == "matematica"):
    os.system("python3 command/italiano/compiti/matematica/mate.py")