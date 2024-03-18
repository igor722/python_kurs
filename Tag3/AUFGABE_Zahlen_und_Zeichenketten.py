while True:
    try:
        zahl = int(input("Bitte ein Zahl zum konvertieren eingeben: "))
        break
    except:
        print("Bitte ein Ganzzahl eingeben")

while True:
    try:
        basis = int(input(
            "Bitte Basis für die Konversion auswählen: \nbinäre Schreibweise: 1\noktale Schreibweise: 8\nhexadezimale Schreibweise: 16\n"))
        if basis == 1:
            konvertierte_zahl = bin(zahl)
            break
        elif basis == 8:
            konvertierte_zahl = oct(zahl)
            break
        elif basis == 16:
            konvertierte_zahl = hex(zahl)
            break
    except:
        print()

if zahl >= 0:
    print(f"Die Zahl {zahl} in Basis {basis} ist: {konvertierte_zahl[2:]}")
else:
    print(
        f"Die Zahl {zahl} in Basis {basis} ist: {konvertierte_zahl[0]}{konvertierte_zahl[3:]}")
