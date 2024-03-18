# Übung »u_operator«
# Das Programm zur Berechnung der Steuer soll wiederum verändert werden (Datei
# u_operator.py). Die Tabelle sieht nun wie folgt aus:
# Gehalt Familienstand Steuersatz
# > 4.000 Euro ledig 26 %
# > 4.000 Euro verheiratet 22 %
# <= 4.000 Euro ledig 22 %
# <= 4.000 Euro verheiratet 18 %

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

while True:
    try:
        eingabe_verheiratet = input("Sind Sie verheiratet? J oder N: ").lower()
    except ValueError:
        continue
    if eingabe_verheiratet != 'j' and eingabe_verheiratet != 'n':
        print("Bitte J oder N eingeben")
        continue
    else:
        break


if eingabe <= 4000 and eingabe_verheiratet == 'n':
    print(f"Ihre Steuerprozent beträgt {steuer2}%")
    print(f"Es ergibt sich eine Steuer von {(eingabe * steuer2 / 100):.2f}€")
elif eingabe <= 4000 and eingabe_verheiratet == 'j':
    print(f"Ihre Steuerprozent beträgt {steuer1}%")
    print(f"Es ergibt sich eine Steuer von {(eingabe * steuer1 / 100):.2f}€")
elif eingabe > 4000 and eingabe_verheiratet == 'n':
    print(f"Ihre Steuerprozent beträgt {steuer3}%")
    print(f"Es ergibt sich eine Steuer von {(eingabe * steuer3 / 100):.2f}€")
else:
    print(f"Ihre Steuerprozent beträgt {steuer2}%")
    print(f"Es ergibt sich eine Steuer von {(eingabe * steuer2 / 100):.2f}€")
