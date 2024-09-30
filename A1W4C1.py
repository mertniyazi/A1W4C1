
def rechtzaak():
    keuze = input("druk iets om verder tegaan: ")

    return keuze


def gevangenis():
    print("b")


def kantine():
    print("c")


def buiten():
    print("d")


while True:
    print("uitleg")
    input("click anything to continue")
    print("begin situatie")
    if rechtzaak() == "accepteren":
        gevangenis()
        break
