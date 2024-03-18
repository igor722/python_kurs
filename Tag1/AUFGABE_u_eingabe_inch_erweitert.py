#Übung »u_eingabe_inch«
#Schreiben Sie ein Programm zur Eingabe und Umrechnung von beliebigen Inch-Werten
#in Zentimeter. Speichern Sie das Programm in der Datei u_eingabe_inch.py. Rufen Sie
#das Programm auf, und testen Sie es. Die Ausgabe kann zum Beispiel wie folgt aussehen:
#Bitte geben Sie den Inch-Wert ein:
#3.5
#3.5 Inch sind 8.89 cm

inch = 2.54

while True:
    auswahl = input("Wilkommen zu cm->inch Rechner \n Bitte auswählen \n drücken \"c\" CM => Inch \n drücken \"i\" Inch => CM   ").lower()
    if auswahl.lower() not in ('c', 'i'):
        print("Falsches Auswahl!")
    else:
        break

if auswahl == 'c':
    eingabe_wert = float(input("Bitte den Wert in cm eingeben: "))
    print(f"{eingabe_wert} cm sind {(eingabe_wert/inch):.2f} inch")
elif auswahl == 'i':
    eingabe_wert = float(input("Bitte den Wert in inch eingeben: "))
    print(f"{eingabe_wert} inch sind {(eingabe_wert*inch):.2f} cm")
