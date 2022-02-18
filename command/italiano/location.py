import os
import webbrowser

location = input("\n che cosa vuoi cercare?: ")

my = ""

if(location == my):
    print(" comndo non valido")
    os.system("python3 command/italiano/location.py")

else:
    webbrowser.open('https://www.google.com/maps/search/' + location)

os.system("python3 language/italiano/console.py")