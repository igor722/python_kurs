# Zur Laufzeit eines Programms Fehler auftreten, die das Programm zum Absturz brinegen
# z.B .: Gibt ein Nutzer bei eind Eingabeaufforderung z.B. eines Text ein, wo eine Zahl
# erwartet wird, sorgen int() und float() für Ausnahme, die das Programm abstürzen lässt
# Dieses Absturzen kann aber "aufgefangen" und behandelt werden
abbruch = False

while not abbruch:
    try:
        zahl = input("Bitte geben Sie eine Zahl ein: ")
        if zahl == "exit":
            abbruch = True
        else:
            zahl = int(zahl)
            print(f"Sie haben die ganze Zahl {zahl} richtig eingegeben")
            abbruch = True
    except:
        print("Fehler bei Umwandlung der Eingabe")

print("Programmende")
