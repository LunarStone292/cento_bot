import webbrowser
import os

print('''\n choice: 
 \n1. translate from english to (language)
 \n2. translate from (language) to english [not avabile] ''')

scelta = int(input("\n select a choice (use the number): "))

if(scelta == 1):
    print('''\n  languages: 
    [WORKING!]
     - Afrikaans
     - Albanian
     - Amharic
     - Arabic
     - Armenian
     - Azerbaijani
     - Basque
     - Bengali
     - Belarusian
     - Burmese
     - Bosnian
     [NOT WORKING!]
     - Bulgarian
     - Catalan
     - Cebuano
     - Czech
     - Chichewa
     - Simplified Chinese
     - Traditional Chinese
     - Korean
     - Course
     - Haitian Creole
     - Croatian
     - Kurdish (Kurmanji)
     - Danish
     - Hebrew
     - Esperanto
     - Estonian
     - Filipino
     - Finnish
     - French
     - Frisian
     - Scottish Gaelic
     - Galician
     - Welsh
     - Georgian
     - Japanese
     - Javanese
     - Greek
     - Gujarati
     - Hausa
     - Hawaiian
     - Hindi
     - Hmong
     - Igbo
     - Indonesian
     - English
     - Irish
     - Icelandic
     - Kannada
     - Kazaro
     - Khmer
     - Kinyarwanda
     - Kyrgyz
     - Lao
     - Latin
     - Latvian
     - Lithuanian
     - Luxembourgish
     - Macedonian
     - Malayalam
     - Malay
     - Malagasy
     - Maltese
     - Maori
     - Marathi
     - Mongolian
     - Nepalese
     - Norwegian
     - Odia (oriya)
     - Dutch
     - Pashto
     - Persian
     - Polish
     - Portuguese
     - Punjabi
     - Romanian
     - Russian
     - Samoan
     - Serbian
     - Sesotho
     - Shona
     - Sindhi
     - Sinhala
     - Slovak
     - Slovenian
     - Somali
     - Spanish
     - Sundanese
     - Swedish
     - Swahili
     - Tajik
     - Thai
     - Tamil
     - Tatar
     - German
     - Telugu
     - Turkish
     - Turkmen
     - Ukrainian
     - Uyghur
     - Hungarian
     - Urdu
     - Uzbek
     - Vietnamese
     - Xhosa
     - Yiddish
     - Yoruba
     - Zulu''')

    lingua = input("\n select the language: ")

    #Afrikaans
    if(lingua == "Afrikaans"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=af&text=' + ling + '&op=translate')
    
    #Albanese
    if(lingua == "Albanian"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=sq&text=' + ling + '&op=translate')
    
    #Amarico
    if(lingua == "Amharic"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=am&text=' + ling + '&op=translate')
    
    #Arabo
    if(lingua == "Arabic"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ar&text=' + ling + '&op=translate')
    
    #Armeno
    if(lingua == "Armenian"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=hy&text=' + ling + '&op=translate')
    
    #Azero
    if(lingua == "Azerbaijani"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=az&text=' + ling + '&op=translate')
    
    #Basco
    if(lingua == "Basque"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=eu&text=' + ling + '&op=translate')
    
    #Bengalese
    if(lingua == "Bengali"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=bn&text=' + ling + '&op=translate')
    
    #Bielorusso
    if(lingua == "Belarusian"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=be&text=' + ling + '&op=translate')
    
    #Birmano
    if(lingua == "Burmese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=my&text=' + ling + '&op=translate')
    
    #Bosniaco
    if(lingua == "Bosnian"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=bs&text=' + ling + '&op=translate')
    
    #Bulgaro
    if(lingua == "Bulgaro"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=bg&text=' + ling + '&op=translate')
    
    #Catalano
    if(lingua == "Catalano"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ca&text=' + ling + '&op=translate')
    
    #Cebuano
    if(lingua == "Cebuano"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ceb&text=' + ling + '&op=translate')
    
    #Ceco
    if(lingua == "Ceco"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=cs&text=' + ling + '&op=translate')
    
    #Chichewa
    if(lingua == "Chichewa"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ny&text=' + ling + '&op=translate')
    
    #Cinese (Semplificato)
    if(lingua == "Cinese (Semplificato)"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=zh-CN&text=' + ling + '&op=translate')
    
    #Cinese (Tradizionale)
    if(lingua == "Cinese (Tradizionale)"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=zh-TW&text=' + ling + '&op=translate')
    
    #Coreano
    if(lingua == "Coreano"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ko&text=' + ling + '&op=translate')
    
    #Corso
    if(lingua == "Corso"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=co&text=' + ling + '&op=translate')
    
    #Creolo haitiano
    if(lingua == "Creolo haitiano"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ht&text=' + ling + '&op=translate')

    #Croato
    if(lingua == "Croato"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=hr&text=' + ling + '&op=translate')
    
    #Curdo (Kurmanji)
    if(lingua == "Curdo (Kurmanji)"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ku&text=' + ling + '&op=translate')

    #Danese
    if(lingua == "Danese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=da&text=' + ling + '&op=translate')
    
    #Ebraico
    if(lingua == "Ebraico"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=iw&text=' + ling + '&op=translate')

    #Esperanto
    if(lingua == "Esperanto"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=eo&text=' + ling + '&op=translate')
    
    #Estone
    if(lingua == "Estone"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=et&text=' + ling + '&op=translate')
    
    #Filippino
    if(lingua == "Filippino"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=tl&text=' + ling + '&op=translate')
    
    #Finlandese
    if(lingua == "Finlandese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=fi&text=' + ling + '&op=translate')
    
    #Francese
    if(lingua == "Francese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=fr&text=' + ling + '&op=translate')
    
    #Frisone
    if(lingua == "Frisone"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=fy&text=' + ling + '&op=translate')

    #Gaelico Scozzese
    if(lingua == "Gaelico Scozzese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=gd&text=' + ling + '&op=translate')

    #Galiziano
    if(lingua == "Galiziano"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=gl&text=' + ling + '&op=translate')
    
    #Gallese
    if(lingua == "Gallese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=cy&text=' + ling + '&op=translate')
    
    #Georgiano
    if(lingua == "Georgiano"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ka&text=' + ling + '&op=translate')
    
    #Giapponese
    if(lingua == "Giapponese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ja&text=' + ling + '&op=translate')
    
    #Giavanese
    if(lingua == "Giavanese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=jw&text=' + ling + '&op=translate')
    
    #Greco
    if(lingua == "Greco"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=el&text=' + ling + '&op=translate')

    #Gujarati
    if(lingua == "Gujarati"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=gu&text=' + ling + '&op=translate')

    #Hausa
    if(lingua == "Hausa"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ha&text=' + ling + '&op=translate')
    
    #Hawaino
    if(lingua == "Hawaino"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=haw&text=' + ling + '&op=translate')

    #Hindi
    if(lingua == "Hindi"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=hi&text=' + ling + '&op=translate')
    
    #Hmong
    if(lingua == "Hmong"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=hmn&text=' + ling + '&op=translate')
    
    #Igbo
    if(lingua == "Igbo"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ig&text=' + ling + '&op=translate')
    
    #Indonesiano
    if(lingua == "Indonesiano"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=id&text=' + ling + '&op=translate')

    #Inglese
    if(lingua == "Inglese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=en&text=' + ling + '&op=translate')

    #Irlandese
    if(lingua == "Irlandese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ga&text=' + ling + '&op=translate')

    #Islandese
    if(lingua == "Islandese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=is&text=' + ling + '&op=translate')

    #Kannada
    if(lingua == "Kannada"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=kn&text=' + ling + '&op=translate')

    #Kazaro
    if(lingua == "Kazaro"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=kk&text=' + ling + '&op=translate')

    #Khmer
    if(lingua == "Khmer"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=km&text=' + ling + '&op=translate')

    #Kinyarwanda
    if(lingua == "Kinyarwanda"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=rw&text=' + ling + '&op=translate')

    #Kirghiso
    if(lingua == "Kirghiso"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ky&text=' + ling + '&op=translate')

    #Lao
    if(lingua == "Lao"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=lo&text=' + ling + '&op=translate')

    #Latino
    if(lingua == "Latino"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=la&text=' + ling + '&op=translate')

    #Lettone
    if(lingua == "Lettone"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=lv&text=' + ling + '&op=translate')

    #Lussemburghese
    if(lingua == "Lussemburghese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=lb&text=' + ling + '&op=translate')

    #Macedone
    if(lingua == "Macedone"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=mk&text=' + ling + '&op=translate')

    #Malayalam
    if(lingua == "Malayalam"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ml&text=' + ling + '&op=translate')
    
    #Malese
    if(lingua == "Malese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ms&text=' + ling + '&op=translate')
    
    #Malgascio
    if(lingua == "Malgascio"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=mg&text=' + ling + '&op=translate')
    
    #Maltese
    if(lingua == "Maltese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=mt&text=' + ling + '&op=translate')
    
    #Maori
    if(lingua == "Maori"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=mi&text=' + ling + '&op=translate')

    #Marathi
    if(lingua == "Marathi"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=mr&text=' + ling + '&op=translate')
    
    #Mongolo
    if(lingua == "Mongolo"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=mn&text=' + ling + '&op=translate')
    
    #Nepalese
    if(lingua == "Nepalese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ne&text=' + ling + '&op=translate')
    
    #Norvegese
    if(lingua == "Norvegese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=no&text=' + ling + '&op=translate')
    
    #Odia (oriya)
    if(lingua == "Odia (oriya)"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=or&text=' + ling + '&op=translate')
    
    #Olandese
    if(lingua == "Olandese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=nl&text=' + ling + '&op=translate')
    
    #Pashto
    if(lingua == "Pashto"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ps&text=' + ling + '&op=translate')
    
    #Persiano
    if(lingua == "Persiano"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=fa&text=' + ling + '&op=translate')
    
    #Polacco
    if(lingua == "Polacco"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=pl&text=' + ling + '&op=translate')
    
    #Portoghese
    if(lingua == "Portoghese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=pt&text=' + ling + '&op=translate')
    
    #Punjabi
    if(lingua == "Punjabi"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=pa&text=' + ling + '&op=translate')
    
    #Rumeno
    if(lingua == "Rumeno"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ro&text=' + ling + '&op=translate')
    
    #Russo
    if(lingua == "Russo"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ru&text=' + ling + '&op=translate')
    
    #Samoano
    if(lingua == "Samoano"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=sm&text=' + ling + '&op=translate')

    #Serbo
    if(lingua == "Serbo"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=sr&text=' + ling + '&op=translate')
    
    #Sesotho
    if(lingua == "Sesotho"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=st&text=' + ling + '&op=translate')
    
    #Shona
    if(lingua == "Shona"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=sn&text=' + ling + '&op=translate')
    
    #Sindhi
    if(lingua == "Sindhi"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=sd&text=' + ling + '&op=translate')
    
    #Singalese
    if(lingua == "Singalese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=si&text=' + ling + '&op=translate')
    
    #Slovacco
    if(lingua == "Slovacco"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=sk&text=' + ling + '&op=translate')
    
    #Sloveno
    if(lingua == "Sloveno"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=sl&text=' + ling + '&op=translate')
    
    #Somalo
    if(lingua == "Somalo"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=so&text=' + ling + '&op=translate')
    
    #Spagnolo
    if(lingua == "Spagnolo"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=es&text=' + ling + '&op=translate')
    
    #Sundanese
    if(lingua == "Sundanese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=su&text=' + ling + '&op=translate')
    
    #Svedese
    if(lingua == "Svedese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=sv&text=' + ling + '&op=translate')
    
    #Swahili
    if(lingua == "Swahili"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=sw&text=' + ling + '&op=translate')
    
    #Tagiko
    if(lingua == "Tagiko"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=tg&text=' + ling + '&op=translate')
    
    #Tailandese
    if(lingua == "Tailandese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=th&text=' + ling + '&op=translate')
    
    #Tamil
    if(lingua == "Tamil"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ta&text=' + ling + '&op=translate')
    
    #Tataro
    if(lingua == "Tataro"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=tt&text=' + ling + '&op=translate')
    
    #Tedesco
    if(lingua == "Tedesco"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=de&text=' + ling + '&op=translate')

    #Telugu
    if(lingua == "Telugu"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=te&text=' + ling + '&op=translate')
    
    #Turco
    if(lingua == "Turco"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=tr&text=' + ling + '&op=translate')
    
    #Turkmeno
    if(lingua == "Turkmeno"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=tk&text=' + ling + '&op=translate')
    
    #Ucraino
    if(lingua == "Ucraino"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=uk&text=' + ling + '&op=translate')
    
    #Uiguro
    if(lingua == "Uiguro"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ug&text=' + ling + '&op=translate')
    
    #Ungherese
    if(lingua == "Ungherese"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=hu&text=' + ling + '&op=translate')
    
    #Urdu
    if(lingua == "Urdu"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=ur&text=' + ling + '&op=translate')
    
    #Uzbeco
    if(lingua == "Uzbeco"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=uz&text=' + ling + '&op=translate')
    
    #Vietnamita
    if(lingua == "Vietnamita"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=vi&text=' + ling + '&op=translate')
    
    #Xhosa
    if(lingua == "Xhosa"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=xh&text=' + ling + '&op=translate')
    
    #Yiddish
    if(lingua == "Yiddish"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=yi&text=' + ling + '&op=translate')
    
    #Yoruba
    if(lingua == "Yoruba"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=yo&text=' + ling + '&op=translate')
    
    #Zulu
    if(lingua == "Zulu"):
        ling = input("\n inserisci cosa tradurre: ")
        webbrowser.open('https://translate.google.com/?rlz=1C1PRFI_enIT892IT892&um=1&ie=UTF-8&hl=it&client=tw-ob&sl=it&tl=zu&text=' + ling + '&op=translate')

os.system("python3 language/italiano/console.py")
