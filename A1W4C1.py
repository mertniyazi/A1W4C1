import time


def rechtzaak():
    print("Rechter: 'U bent hier vandaag omdat u schuldig bent bevonden aan de moord op de 10-jarige Bram.'")
    print("Kunt u deze actie rechtvaardigen?")
    time.sleep(2)
    print("Onder immense druk zitten je gedachten en zenuwen, waardoor je twijfelt tussen wegrennen of de straf accepteren... Misschien zou het liegen wel kunnen slagen?")
    time.sleep(4)
    keuze_rechtzaak = input('''Welke optie van de drie neem je?
    - Accepteren
    - Liegen
    - Wegrennen
    Kies: ''').lower()

    if keuze_rechtzaak == "accepteren":
        print("Je hebt jouw daad geaccepteerd en krijgt 20 jaar celstraf voor het vermoorden van de 10-jarige Bram.")
        return True
    elif keuze_rechtzaak == "wegrennen":
        print("Je probeert weg te rennen als een idioot en wordt getackeld door een politieagent.")
        return True
    elif keuze_rechtzaak == "liegen":
        print("Omdat je loog tijdens een serieuze rechtszaak, word je veroordeeld tot levenslang en kom je nooit meer vrij.")
        return False
    else:
        print("Voer een geldige keuze in.")


def gevangenis():
    print("Nadat je werd veroordeeld ga je naar de gevangenis daar zie je cel waar je de komende 20 jaar zal moeten leven")
    time.sleep(2)
    print("Gevangenisbewaker: 'Zo we zijn er, dit is je nieuwe thuis geniet'")
    time.sleep(2)
    print("Je zit nu te bedenken van hoe je kan ontsnappen van jou cel")
    print("Je zit nu te bedenken misschien is de deur wel open of misschien kan ik wachten op mijn eten want je kan niet goed nadenken met een legen maag")
    print("of ik kan een drillboor paken naast de cel en mijn weg doorboren.")
    time.sleep(4)
    keuze_gevangenis = input('''Welke optie van de drie neem je?
    - Cel openen
    - Wachten
    - Drillen
    Kies: ''').lower()

    if keuze_gevangenis == "cel openen":
        print("de gevangenisbewaker had vergeten de deur op slot te zetten en je kan makkelijk weglopen naar de kantine.")
        return True
    elif keuze_gevangenis == "wachten":
        print("Je wacht op jou eten en tijdens het eten vergeet je om te ontsnappen.")
        return False
    elif keuze_gevangenis == "drillen":
        print("Je pakt de drillboor en begint te drillen je hebt een groot gat gemaakt om er doorheen te springen.")
        time.sleep(2)
        print("Terwijl je springt besef je dat onder jou een politie bureau en dat het te laat is om omhoog te staan")
        print("er staan ook 6 bewakers die naast jou staan en ze zijn boos dat je hun koffie pauze hebt verstoord en ze slaan jou helemaal kapot.")
        time.sleep(1)
        print("je gaat terug in jou cel")
        return False
    else:
        print("Voer een geldige keuze in.")


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
    print("Je bent nu buiten, maar je bent nog niet helemaal vrij.")
    print("Je kijkt om je heen en je ziet een politie bus, een hek en een slaperige politie agent.")
    time.sleep(1)
    print("Je zit nu te bedenken van hoe je het wilt doen")
    print("Je ziet de politie bus we genoeg ruimte heeft om eronder te verstoppen")
    time.sleep(1)
    print("Je kijkt ook naar de hek")
    print("Je ziet dat de hek best wel makkelijk is om erover heen te klimmen en ook best laag is.")
    time.sleep(1)
    print("Je kijk ook naar de slaperige politie agent en denk van dat je de politie agent wel aankan pakken en zijn uniform stelen.")
    time.sleep(4)
    keuze_buiten = input('''Welke optie van de drie neem je?
    - Verstoppen 
    - Klimmen
    - Uniform stelen
    Kies: ''').lower()

    if keuze_buiten == "verstoppen":
        print("Je zit stiekem te kruipen en je bent onder de bus")
        time.sleep(2)
        print("Je wacht heel lang het voelt alsof het een eewigheid duurt")
        print("Je denkt om weer terug te gaan naar de voorkant van de gebouw")
        time.sleep(1)
        print("Je hoort opeens een motor")
        print("Het is de motor van de politie bus")
        print("Je bent nu aan het bewegen.")
        time.sleep(2)
        print("Je bent ontsnapt!")
        return True
    elif keuze_buiten == "klimmen":
        print("Je besluit te onsnappen door middel van klimmen.")
        print("Je bent stiekem naar de hek aan het lopen.")
        time.sleep(1)
        print("Je bent bij de hek.")
        print("Je springt op het hek om te klimmen.")
        time.sleep(1)
        print("Wanneer je op de hek bent voel je een shrok.")
        time.sleep(1)
        print("Het was de hek")
        print("Je kijkt naar links en er staat een gevaren teken van 10000 volt die had je niet gezien.")
        print("je bent geëlektrocuteerd en door de hoge volt ben de dood gegaan door een hartstilstand.")
        return False
    elif keuze_buiten == "uniform stelen":
        print("Je hebt besloten om de uniform te stelen van de slaperige agent.")
        time.sleep(1)
        print("Je rent op de agent en probeerd hem aantevallen")
        print("Wat je niet wist was dat de agent altijd slaperig eruit ziet, maar hij is klaarwaker en hij hoort jou rennen")
        time.sleep(1)
        print("De agent draaid zich om en pakt zijn wapen.")
        time.sleep(1)
        print("BANG! BANG!")
        print("De agent schiet twee kogels en heeft jou geraakt.")
        print("De agent komt naar jou toe en zegt:")
        time.sleep(1)
        print("agent:'Wat een idioot'")
        print("Je bent dood geschoten.")
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
print("Je blijkt verwikkeld te zijn in een rechtszaak.")

while True:
    recht = rechtzaak()
    if recht == "accepteren":
        gevangenis()
        break
    elif recht == "weg rennen":
        gevangenis()
        break
    elif recht == "liegen":
        print("Omdat je zat te liegen tijdens een serieuze rechtzaak wordt je veroordeeld voor maximaal levenseis en je kan er nooit meer eruit.")
    else:
        print("Voer een valide keuze in.")
