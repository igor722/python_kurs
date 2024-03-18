# Übung »u_datum«
# Entwickeln Sie ein Programm zur Prüfung einer Datumsangabe (Datei u_datum.py). Der
# Benutzer soll die drei Bestandteile eines Datums einzeln eingeben. Anschließend wird
# ermittelt, ob es sich um ein falsches oder ein richtiges Datum handelt. Gehen Sie bei der
# Entwicklung wie nachfolgend beschrieben vor. Testen Sie Ihr Programm nach jedem
# Schritt:
#  Untersuchen Sie den eingegebenen Wert für den Tag. Ist er kleiner als 1 oder größer
# als 31, handelt es sich um ein falsches Datum.
#  Untersuchen Sie den eingegebenen Wert für den Monat. Ist er kleiner als 1 oder grö-
# ßer als 12, handelt es sich um ein falsches Datum.
#  Geben Sie den Wert aus, den der letzte Tag des betreffenden Monats hat. Denken Sie
# daran, dass es nur drei mögliche Fälle gibt: 28, 30 oder 31 Tage. Die Regeln für Schalt￾jahre werden noch nicht beachtet.
#  Untersuchen Sie den eingegebenen Wert für den Tag. Geben Sie aus, ob er kleiner als
# 1 oder größer als der letzte Tag des betreffenden Monats ist.
#  Untersuchen Sie den eingegebenen Wert für das Jahr. Geben Sie aus, ob es sich um
# ein Schaltjahr handelt. Die vereinfachte Regel für ein Schaltjahr lautet: Lässt sich der
# Wert ohne Rest durch 4 teilen, handelt es sich um ein Schaltjahr.
#  Kombinieren Sie die bisherigen Schritte miteinander. Ist der Wert für den Tag kleiner
# als 1 oder größer als der letzte Tag des betreffenden Monats (mit Berücksichtigung
# der Regel für ein Schaltjahr), handelt es sich um ein falsches Datum, ansonsten um
# ein richtiges Datum.
#  Erweitern Sie das Programm. Die vollständige Regel für ein Schaltjahr lautet: Lässt
# sich der Wert ohne Rest durch 4 teilen, aber nicht ohne Rest durch 100, handelt es
# sich um ein Schaltjahr. Es handelt sich aber auch um ein Schaltjahr, falls sich der
# Wert ohne Rest durch 400 teilen lässt.
# Ein Aufruf des fertigen Programms könnte wie folgt aussehen:
# Tag des Datums eingeben:
# 29
# Monat des Datums eingeben:
# 2
# Jahr des Datums eingeben:
# 2000
# Letzter Tag: 29
# Richtiges Datum

while True:
    try:
        eingabe_tag = int(input("Bitte Tag eingeben: "))
        eingabe_monat = int(input("Bitte Monat eingeben: "))
        eingabe_jahr = int(input("Bitte Jahr eingeben: "))
    except ValueError:
        print("Bitte eine Zahl eingeben")

    # Tag Logik
    if eingabe_tag <= 0 or eingabe_tag > 31:
        print("Bitte eine gültige Tag eingeben")
        continue
    # Monat Logik
    if eingabe_monat <= 0 or eingabe_monat > 12:
        print("Bitte eine gültige Monat eingeben")
        continue

    else:
        break


# Schaltjahr Logik
if eingabe_jahr % 4 == 0 and eingabe_jahr % 100 != 0 and eingabe_monat == 2 and eingabe_tag > 29:
    print(f"{eingabe_jahr} ist ein Schaltjahr. Februar in Schaltjahr kann höchstens 29 Tage haben.")
# Februar logik
elif eingabe_jahr % 4 != 0 and eingabe_monat == 2 and eingabe_tag > 28:
    print("Februar kann höchstens 28 Tage haben")

# kurzere Monate Logik
elif eingabe_monat in [4, 6, 9, 11] and eingabe_tag == 31:
    print("Bitte eine gültige Tag eingeben")

else:
    # führende Null/BC/AC
    # tag
    if eingabe_tag < 10:
        zeige_tag = '0' + str(eingabe_tag)
    else:
        zeige_tag = eingabe_tag
    # monat
    if eingabe_monat < 10:
        zeige_monat = '0' + str(eingabe_monat)
    else:
        zeige_monat = eingabe_monat

    if eingabe_jahr < 0:
        eingabe_jahr = eingabe_jahr * (-1)
        zeige_jahr = str(eingabe_jahr) + ' BC'
    else:
        zeige_jahr = eingabe_jahr
    print(
        f"Eingegebene Datum {zeige_tag}.{zeige_monat}.{zeige_jahr} ist richtig")
