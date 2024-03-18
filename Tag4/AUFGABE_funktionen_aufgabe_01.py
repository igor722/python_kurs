# Aufgabe 01
# Schreiben Sie eine Python-Funktion finde_naechste_zahl, die drei ganzen Zahlen entgegen-
# nimmt: ziel, zahl1 und zahl2. Die Funktion soll ermitteln, welche der beiden Zahlen (zahl1
# oder zahl2) dem Wert ziel am nächsten liegt und das Ergebnis entsprechend ausgeben. Wenn
# beide Zahlen gleich weit vom Ziel entfernt sind, soll die Funktion zahl1 ausgeben.
# Rufen Sie die Funktion jeweils mit folgenden Beispielen auf
# finde_naechste_zahl(10, 8, 12
# # Gibt 8 ausgeben, da 8 näher an 10 liegt als 12
# finde_naechste_zahl(10, 9, 11) # Sollte 9 oder 11 ausgeben; beide sind gleich weit entfernt,
# also wird 9 zurückgegeben

def finde_naechste_zahl(ziel, zahl1, zahl2):

    entfernung1 = ziel - zahl1
    if entfernung1 < 0:
        entfernung1 = entfernung1 * -1

    entfernung2 = ziel - zahl2
    if entfernung2 < 0:
        entfernung2 = entfernung2 * -1

    print(f"Weniger entfernt vom {ziel} ist Zahl: ", end="")
    if entfernung1 < entfernung2:
        print(zahl1)
    elif entfernung2 < entfernung1:
        print(zahl2)
    else:
        print(zahl1)


finde_naechste_zahl(10, 5, 9)
