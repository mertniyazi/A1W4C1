def rechtzaak():
    print("a")
    keuze = input("druk iets om verder tegaan: ")
    print("m")
    return keuze


def gevangenis():
    print("b")


def kantine():
    print("c")


def buiten():
    print("d")


while True:
    if rechtzaak() == "accepteren":
        gevangenis()
        break
