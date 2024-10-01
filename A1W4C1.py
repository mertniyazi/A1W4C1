import time


def rechtzaak():
    keuze_rechtzaak = input(
        "typ 1 van de 3 opties(accepteren, weg rennen of liegen): ").lower()
    if keuze_rechtzaak == "accepteren":
        print(f"Je hebt jou daad geaccepteerd er krijgt 20 jaar celstraf van het beroven van een oude vrouw.")
        return True
    elif keuze_rechtzaak == "weg rennen":
        print(f"Je probeert weg te rennen als een mogool en wordt getackeld door een politie agent.")
        return True
    elif keuze_rechtzaak == "liegen":
        print(f"Omdat je zat te liegen tijdens een serieuze rechtzaak wordt je veroordeeld voor maximaal levenseis en je kan er nooit meer eruit.")
        return False
    else:
        print(f"Voer een valide keuze in.")


def gevangenis():
    keuze_gevangenis = input(
        "typ 1 van de 3 opties(accepteren, weg rennen of liegen): ").lower()
    if keuze_gevangenis == "accepteren":
        print(f"Je hebt jou daad geaccepteerd er krijgt 20 jaar celstraf van het beroven van een oude vrouw.")
        return True
    elif keuze_gevangenis == "weg rennen":
        print(f"Je probeert weg te rennen als een mogool en wordt getackeld door een politie agent.")
        return True
    elif keuze_gevangenis == "liegen":
        print(f"Omdat je zat te liegen tijdens een serieuze rechtzaak wordt je veroordeeld voor maximaal levenseis en je kan er nooit meer eruit.")
        return False
    else:
        print(f"Voer een valide keuze in.")


def kantine():
    keuze_kantine = input("")


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
