
def rechtzaak():
    keuze_rechtzaak = input("druk iets om verder tegaan: ")

    return keuze_rechtzaak


def gevangenis():
    keuze_gevangenis = input("Voer een keuze in: ")
    if keuze_gevangenis == "Drillboor":
        print("Je valt in de politie bureau")


def kantine():
    print("c")


def buiten():
    print("d")


print("uitleg")
input("click anything to continue")
print("begin situatie")
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
