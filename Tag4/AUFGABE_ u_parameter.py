# Übung »u_parameter«
# Es soll wiederum die Steuer für verschiedene Gehälter berechnet werden (Datei u_para￾meter.py). Liegt das Gehalt über 2.500 Euro, sind 22 % Steuern zu zahlen, ansonsten 18 %.
# Die Berechnung und die Ausgabe der Steuer sollen diesmal innerhalb einer Funktion mit
# dem Namen steuer() stattfinden. Die Funktion soll für die folgenden Gehälter aufgeru￾fen werden: 1.800 Euro, 2.200 Euro, 2.500 Euro, 2.900 Euro.


gehalt = int(input("Bitte in € eingeben: "))


def steuer():
    steuer1 = 22
    steuer2 = 18

    if gehalt > 2500:
        print(f"Steuer: {steuer1}%, Betrag: {gehalt*steuer1/100}€")
    else:
        print(f"Steuer: {steuer2}%, Betrag: {gehalt*steuer2/100}€")


if gehalt in [1800, 2200, 2500, 2900]:
    steuer()
else:
    print("Steuer kann nicht ausgerechnet werden")
