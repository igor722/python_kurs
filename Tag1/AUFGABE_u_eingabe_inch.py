#Übung »u_eingabe_inch«
#Schreiben Sie ein Programm zur Eingabe und Umrechnung von beliebigen Inch-Werten
#in Zentimeter. Speichern Sie das Programm in der Datei u_eingabe_inch.py. Rufen Sie
#das Programm auf, und testen Sie es. Die Ausgabe kann zum Beispiel wie folgt aussehen:
#Bitte geben Sie den Inch-Wert ein:
#3.5
#3.5 Inch sind 8.89 cm

inch = 2.54
print("cm in inch Rechner")
eingabe_inch = float(input("Bitte den Wert in inch eingeben: "))
print(f"{eingabe_inch} Inch sind {eingabe_inch*inch} cm")