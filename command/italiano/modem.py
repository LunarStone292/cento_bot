import os
import platform
import webbrowser

ricerca = input("\n inserisci cosa vuoi cercare: ")

ricerca_google = "https://www.google.com/search?q=" + ricerca + "&rlz=1C1PRFI_enIT892IT892&ei=OzbxYa71DfKI9u8PsKCF4As&ved=0ahUKEwju_oTOrc_1AhVyhP0HHTBQAbwQ4dUDCA4&uact=5&oq=lol+a&gs_lcp=Cgdnd3Mtd2l6EAMyBAguEEMyBwgAELEDEEMyBwgAELEDEEMyCwguEIAEELEDEIMBMgsILhCABBCxAxCDATIFCAAQgAQyBAgAEEMyCAgAEIAEELEDMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwE6BwgAEEcQsAM6BwgAELADEEM6CQgAELADEAoQQzoKCAAQ5AIQsAMYADoMCC4QyAMQsAMQQxgBSgQIQRgASgQIRhgBUMYBWJ0EYI8FaAFwAngAgAFgiAFgkgEBMZgBAKABAcgBE8ABAdoBBggAEAEYCdoBBggBEAEYCA&sclient=gws-wiz"
if(platform.system() == "Windows"):
    webbrowser.open(ricerca_google)
else:
    os.system(ricerca_google)

os.system("python3 language/italiano/console.py")
