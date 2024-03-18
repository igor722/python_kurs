#Übung »u_verzweigung_mehrfach«
#Das Programm zur Berechnung der Steuer soll weiter verändert werden (Datei u_verzweigung_mehrfach.py).
#Der Anwender soll sein monatliches Gehalt eingeben. Anschließend wird seine Steuer nach der folgenden Tabelle berechnet:
#Gehalt Steuersatz
#mehr als 4.000 Euro 26 %
#2.500 bis 4.000 Euro 22 %
#weniger als 2.500 Euro 18 %

steuer1 = 18
steuer2 = 22
steuer3 = 26

while True:
    try:
        eingabe = float(input("Geben Sie Ihr Gehalt in Euro ein: "))
    except ValueError:
        print("Bitte eine Zahl eingeben")
        continue
    if eingabe <= 0:
        print("Sie haben eine negative Wert oder 0 eingegeben")
        continue
    else:
        break


if eingabe > 0 and eingabe <= 2500:
    print(f"Es ergibt sich eine Steuer von {(eingabe * steuer1 / 100):.2f}€")
elif eingabe > 2500 and eingabe <= 4000:
    print(f"Es ergibt sich eine Steuer von {(eingabe * steuer2 / 100):.2f}€")
elif eingabe > 4000:
    print(f"Es ergibt sich eine Steuer von {(eingabe * steuer3 / 100):.2f}€")
