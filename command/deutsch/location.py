import os
import webbrowser

location = input("\n wonach willst du suchen?: ")

my = ""

if(location == my):
    print(" ungültiger Befehl")
    os.system("python3 command/deutsch/location.py")

else:
    webbrowser.open('https://www.google.com/maps/search/' + location)

os.system("python3 language/deutsch/console.py")