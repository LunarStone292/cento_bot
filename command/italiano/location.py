import os
from platform import platform
import webbrowser

location = input("\n che cosa vuoi cercare?: ")

my = ""

if(location == my):
    print(" comndo non valido")
    os.system("python3 command/italiano/location.py")

else:
    if(platform.system() == "Windows"):
        webbrowser.open('https://www.google.com/maps/search/' + location)
    else:
        os.system("firefox https://www.google.com/maps/search/" + location)

os.system("python3 language/italiano/console.py")
