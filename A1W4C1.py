import time


def ascii_rechtzaak():
    print('''
          ```
Kunt u deze actie rechtvaardigen?
                      Hmmm...
                        \          `,
                                ___ #
                                |/  ?
            .......             | , )\
                 /              /__/\ \____               #####
                           ,-   /   \_/    \            _/_ ####
          /\,_\          |/|   / < _____ _> \          [.[.]-=##
          )   "\        -|.|--/___/  ,___/___\-         /_    )#
          \ ___Y.   _____'-'______|\/______________     |__   #
         __)/      [_______________________________]     \___/
        /)  \       |                             |     .'\$/\`-.
       /|| .|       |            _...._           |    ( `.Y.' ( )
    __;_||__|_______|         ,-' ALT. '-_        |____|:__o___|_|_
   [________________|        /   ASCII-   \       |________________]
    |               |       |  _ _ART  ____.      |               |
    |   Balif       |       | / / \| ||_)| |      |               |
    |   RALF        |        \\_\_/|_|| \|/       |               |
____|               |         -_        ,-        |               |____
    |               |           `-...,-'          |               |
    |               |                             |               |
    |_______________|_____________________________|_______________|```\n''')


def kantine():
    print("Je bent nu in de kantine je weet dat je bijna bij de uitgang bent, maar je wilt ook snel wat eten.")
    time.sleep(2)
    print("Hopeloos zit je in de kantine maar je hebt ook honger je zit nu in een dilemma zou ik eten of zou ik verder rennen misschien is de kantine deur ook open.")
    print("Je ziet 2 dingen om te eten.")
    time.sleep(1)
    print("Je ziet een paarse fruit die op een anime fruit lijkt.")
    time.sleep(1)
    print("Je ziet de smerige puree die echt heel smerig deruit ziet.")
    time.sleep(1)
    print("Je zit nu te bedenken van hoe je het wilt doen ga ik eten of zou ik verder rennen.")
    time.sleep(4)
    keuze_kantine = input('''Welke optie van de drie neem je?
    - Devil fruit
    - Puree
    - verder rennen
    Kies: ''').lower()

    if keuze_kantine == "devil fruit":
        print("Je eet de paarse fruit en merkt meteen dat het een devil fruit is van One Piece.")
        time.sleep(1)
        print("Je neemt een hap van de fruit en voelt iets.")
        time.sleep(2)
        print("Je beseft je heel snel dat je niet in een anime zit en dat je jezelf hebt vergiftigt.")
        print("Je beseft je ook meteen dat je heel dom bent en het gewoon een bedorve appel is.")
        time.sleep(1)
        print("Je zit daar met buikpijn en diarree in de midden van de kantine.")
        return False
    elif keuze_kantine == "puree":
        print("Je eet met tegenzin de puree je.")
        print("Je neemt een hap van de walgelijke puree je voelt daarna iets in je mond.")
        time.sleep(1)
        print("Het is een sleutel!")
        print("Je loopt na het vinden van de sleutel naar de kantine deur.")
        time.sleep(2)
        print("De kantine deur gaat open.")
        time.sleep(1)
        print("Je kijkt links en recht en gaat stiekem naar buiten")
        time.sleep(1)
        print("Je bent buiten!")
        return True
    elif keuze_kantine == "verder rennen":
        print("Je beslist om verder te rennen.")
        time.sleep(1)
        print("Je bent bij de kantine deur en probeerd het open te maken")
        time.sleep(1)
        print("De deur is op slot!")
        time.sleep(1)
        print("je gaat weer naar het midden van de kantine en zit nu te bedenken van hoe je wilt ontsnappen.")
        return False
    else:
        print("Voer een geldige keuze in.")


def buiten():
    print("Je bent nu buiten, maar nog niet helemaal vrij.")
    print("Om je heen zie je een politiebus, een hek, en een slaperige politieagent.")
    time.sleep(1)
    print("Je denkt na over hoe je wilt ontsnappen.")
    print("De politiebus heeft genoeg ruimte om je eronder te verstoppen.")
    time.sleep(1)
    print("Het hek lijkt makkelijk over te klimmen, het is niet zo hoog.")
    time.sleep(1)
    print("De politieagent lijkt versuft. Je denkt eraan om hem te overmeesteren en zijn uniform te stelen.")
    time.sleep(4)

    keuze_buiten = input('''Welke optie kies je?
    - Verstoppen
    - Klimmen
    - Uniform stelen
    Kies: ''').lower()

    if keuze_buiten == "verstoppen":
        print("Je kruipt stilletjes onder de bus.")
        time.sleep(2)
        print("Het wachten voelt als een eeuwigheid.")
        print("Je denkt eraan terug te gaan naar het gebouw.")
        time.sleep(1)
        print("Opeens hoor je een motor starten.")
        print("De bus begint te rijden. Je bent ontsnapt!")
        return True

    elif keuze_buiten == "klimmen":
        print("Je besluit te ontsnappen door te klimmen.")
        print("Stilletjes nader je het hek.")
        time.sleep(1)
        print("Je bent bij het hek en begint te klimmen.")
        time.sleep(1)
        print("Plotseling voel je een schok.")
        time.sleep(1)
        print("Het hek staat onder stroom!")
        print("Er hangt een bordje: '10000 volt'. Dat had je niet gezien.")
        print("Je wordt geÃ«lektrocuteerd en sterft aan een hartstilstand.")
        return False

    elif keuze_buiten == "uniform stelen":
        print("Je besluit het uniform van de agent te stelen.")
        time.sleep(1)
        print("Je rent op de agent af en probeert hem te overmeesteren.")
        print("Wat je niet wist, is dat hij wel alert is en je voetstappen hoort.")
        time.sleep(1)
        print("De agent draait zich om en trekt zijn wapen.")
        time.sleep(1)
        print("BANG! BANG!")
        print("Je wordt geraakt door twee kogels.")
        time.sleep(1)
        print("De agent komt naar je toe en zegt spottend:")
        print("Agent: 'Wat een idioot.'")
        print("Je bent doodgeschoten.")
        return False

    else:
        print("Voer een geldige keuze in.")


def gevangenis():
    print("Na de rechtszaak beland je in een gevangenis en zie je daar je cel waar je de komende 20 jaar zult moeten leven in schuld.")
    time.sleep(2)
    print("Gevangenisbewaker: 'Zo we zijn er, dit is je nieuwe thuis geniet ervan.'")
    time.sleep(5)
    print("Je zit nu te bedenken van hoe je kan ontsnappen van jouw cel.")
    print("Je denkt nu dat de deur misschien voor je open is gelaten of dat ik misschien op mijn eten kan wachten, want je lijkt niet goed te kunnen nadenken met een lege maag.")
    print("Of kan ik misschien zelf ontsnappen met een boor?")
    time.sleep(4)
    keuze_rechtzaak = input('''Welke optie van de drie neem je?
    - Cel openen
    - Wachten
    - Drillen
    Kies: ''').lower()

    if keuze_rechtzaak == "cel openen":
        print("De gevangenisbewaker was vergeten de deur op slot te doen en je kunt gemakkelijk weglopen naar de kantine...")
        return True
    elif keuze_rechtzaak == "wachten":
        print("Je hoort geklop op je deur, voordat je eten naar binnen wordt geschoven en je ervan eet.")
        time.sleep(5)
        print("Je bent dood gegaan door vergiftigd eten en begint opnieuw.")
        time.sleep(5)
        return False
    elif keuze_rechtzaak == "drillen":
        print("Je vindt een boor onder het bed van jouw celgenoot en begint te boren.")
        time.sleep(4)
        print("Terwijl je springt, realiseer je je dat je in de lunchruimte van de politie valt en dat het te laat is om je keuze terug te nemen.")
        print("Er staan 6 bewakers die naast jou staan en ze zijn boos dat je hun koffie pauze hebt verstoord en ze slaan jou helemaal kapot.")
        time.sleep(5)
        print("Je gaat terug de cel in en begint opnieuw.")
        time.sleep(5)
        return False
    else:
        print("Voer een geldige keuze in.")


def rechtzaak():
    print("Rechter: 'U bent hier vandaag omdat u schuldig bent bevonden aan de moord op de 10-jarige Bram.'")
    print("Kunt u deze actie rechtvaardigen?")
    time.sleep(4)
    print("Onder immense druk zitten je gedachten en zenuwen, waardoor je twijfelt tussen wegrennen of de straf accepteren... Misschien zou het liegen wel kunnen slagen?")
    time.sleep(3)
    ascii_rechtzaak()
    time.sleep(2)
    keuze_rechtzaak = input('''Welke optie van de drie neem je?
    - Accepteren
    - Liegen
    - Wegrennen
    Kies: ''').lower()

    if keuze_rechtzaak == "accepteren":
        print("Je hebt je daad geaccepteerd en krijgt 20 jaar gevangenisstraf voor het vermoorden van de 10-jarige Bram.")
        return True
    elif keuze_rechtzaak == "wegrennen":
        print("Je probeert als een idioot weg te rennen en wordt getackeld door een politieagent!")
        time.sleep(5)
        return True
    elif keuze_rechtzaak == "liegen":
        print("Omdat je gelogen hebt tijdens een ernstig proces, word je veroordeeld tot levenslang en kom je nooit meer vrij.")
        return False
    else:
        print("Voer een geldige keuze in.")


print('''
Vanaf het begin bevindt de speler zich in een moeilijke situatie.
Hij krijgt een aantal opties voorgeschoteld, waarvan sommige goed en sommige fout zijn.
Om het spel te verslaan, moet de speler de juiste volgorde vinden door telkens het juiste te kiezen.
''')

input("Druk op enter om verder te gaan.\n")

print("Je staat in een positie waarbij je naar beneden kijkt en stemmen weerklinken door de kamer...")
time.sleep(4)
print("Na een tijdje worden de stemmen steeds luider om je heen, voordat plotseling de oorverdovende stilte in de hal je doet schrikken.")
time.sleep(3)
print("KLAK KLAK! 'Stilte in de zaal!' schreeuwt de rechter met de slaande hammer.")
time.sleep(1)
print("Je blijkt verwikkeld te zijn in een rechtszaak.\n")

input("Druk op enter om verder te gaan.\n")

while True:
    if rechtzaak():
        print('''
Na een paar dagen ontwaak je in een cel van een gevangenis...
Het enige licht schijnt van boven, afkomstig van een oude hanglamp die aan een draad bungelt, maar op het punt staat te vallen en kapot te gaan.''')
        time.sleep(4)

        print("Je staat langzaam op en kijkt om je heen, waardoor je langzaam tot jezelf komt en alles om je heen in je opneemt.")
        print("Je voelt de drang om te huilen, maar bij het kijken in de spiegel zie je dat je ogen al vermoeid zijn van het huilen.")
        time.sleep(4)

        while True:
            if gevangenis():
                break
            else:
                time.sleep(5)
                print("Je krijgt een nieuwe kans om je keuzes te heroverwegen.")
                time.sleep(4)

        while True:
            if kantine():
                break
            else:
                time.sleep(5)
                print("Je krijgt een nieuwe kans om je keuzes te heroverwegen.")
                time.sleep(4)

        while True:
            if buiten():
                break
            else:
                time.sleep(5)
                print("Je krijgt een nieuwe kans om je keuzes te heroverwegen.")
                time.sleep(4)
    else:
        time.sleep(5)
        print("Het blijkt dat je terug in de tijd gaat, een nieuwe kans om iets beters te kiezen.")
        time.sleep(4)

    break
