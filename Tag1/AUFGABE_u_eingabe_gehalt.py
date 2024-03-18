#Übung »u_eingabe_gehalt«
#Schreiben Sie ein Programm zur vereinfachten Berechnung der Steuer. Der Anwender
#wird dazu aufgefordert, sein monatliches Gehalt einzugeben. Anschließend werden 18 %
#dieses Betrags berechnet und ausgegeben. Nutzen Sie die Datei u_eingabe_gehalt.py.
#Die Ausgabe kann zum Beispiel wie folgt aussehen:
#Geben Sie Ihr Gehalt in Euro ein:
#2500
#Es ergibt sich eine Steuer von 450.0 Euro

prozent = 18


eingabe_gehalt = float(input("Geben Sie Ihr Gehalt in Euro ein: "))
steuer = eingabe_gehalt * prozent / 100
print(f"Es ergibt sich eine Steuer von {steuer} Euro")