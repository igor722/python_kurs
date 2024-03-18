# Übung »u_fehler«
# Verbessern Sie das Programm zur Eingabe und Umrechnung eines beliebigen Inch￾Werts in Zentimeter. Die Folgen eines Eingabefehlers des Anwenders sollen abgefangen
# werden. Das Programm soll den Anwender so lange zur Eingabe auffordern, bis sie er￾folgreich war (Datei u_fehler.py).

inch = 2.54

while True:
    auswahl = input(
        "Wilkommen zu cm->inch Rechner \n Bitte auswählen \n drücken \"c\" CM => Inch \n drücken \"i\" Inch => CM   ").lower()
    if auswahl.lower() not in ('c', 'i'):
        print("Falsches Auswahl!")
    else:
        break

if auswahl == 'c':
    while True:
        try:
            eingabe_wert = float(input("Bitte den Wert in cm eingeben: "))
            print(f"{eingabe_wert} cm sind {(eingabe_wert/inch):.2f} inch")
            break
        except:
            print("Bitte eine Zahl eingeben!")
elif auswahl == 'i':
    while True:
        try:
            eingabe_wert = float(input("Bitte den Wert in inch eingeben: "))
            print(f"{eingabe_wert} inch sind {(eingabe_wert*inch):.2f} cm")
            break
        except:
            print("Bitte eine Zahl eingeben!")

print("============Programmende============")
