
def rechtzaak():
    keuze = input("druk iets om verder tegaan: ")

    return keuze


def gevangenis():
    print("b")


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
        break
    else:
        print("Voer een valide keuze in.")
