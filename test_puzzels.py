import time


def puzzel_1():
    # print("""\

    #                 """)
    print("omdat we nu bij de onderdeel van een rechtzaak zijn")
    print("Gaan we jou knowledge teste of je uberhaubt de weten weet van Nederland")
    time.sleep(2)
    print('''Waarom is nederland een rechtsstaat
    - (1)Iedereen moet zich aan de wet houden 
    - (2)
    - (3)Nederland is geen rechtstaat maar een  land
    Kies: ''')
    antwoord_puzzel_1 = int(input('Voer 1, 2 of 3 in'))

    if antwoord_puzzel_1 == 1:
        return print("Dat is correct iedereen is gelijk volgens de wet")
    elif antwoord_puzzel_1 == 2:
        print("")
