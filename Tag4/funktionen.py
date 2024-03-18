def gruesse_alle():
    print("Ich grüße dich und die ganze Welt!")


gruesse_alle()


def gruesse_dich(name):
    print(f"Hallo {name}, ich grüße auch besonders dich!")


gruesse_dich("Igor")


def quadrat(zahl):
    quadrat = zahl * zahl
    print(f"Zahl: {zahl}, Quadrat: {quadrat}")


quadrat(4)


def berechnung(x, y, z):
    ergebnis = (x + y) * z
    print("Ergebnis: ", ergebnis)


berechnung(2, 4, 6)
berechnung(8, 2, 2)


def mittelwert(x, y):
    ergebnis = (x + y) / 2
    print("Mittelwert: ", ergebnis)


mw = mittelwert(2, 5)


def volumen(breite, laenge, tiefe, farbe):
    print("Werte:", breite, laenge, tiefe, farbe)
    print("Volumen: ", breite * laenge * tiefe, "Farbe: ", farbe)


volumen(2, 5, 4, "rot")
volumen(laenge=2, farbe="gelb", tiefe=3, breite=4)

# Optionale Parameter
# ermögliche eine variable Parameteranzahl
# Sie müssen ein Vorgabewert (mit = zugewiesener Wert in der Parameterliste
# erhalten und am Ende der Parameterliste stehen
# Kann mit benannten Parametern kombiniert werden


def volumen(breite, laenge, tiefe=1, farbe="schwarz"):
    print("Werte:", breite, laenge, tiefe, farbe)
    print("Volumen: ", breite * laenge * tiefe, ", Farbe: ", farbe)


volumen(2, 5, 4, "rot")
volumen(2, 12, 8)
