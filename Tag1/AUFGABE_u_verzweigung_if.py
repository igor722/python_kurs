#Übung »u_verzweigung_if«
#Das vereinfachte Programm zur Berechnung der Steuer wird verändert. Der Anwender
#soll dazu aufgefordert werden, sein monatliches Gehalt einzugeben. Liegt es über 2.500
#Euro, sind 22 % Steuern zu zahlen, ansonsten 18 %. Nutzen Sie die Datei u_verzweigung_
#if.py.
#Es ist nur eine Eingabe erforderlich. Innerhalb des Programms soll anhand des Gehalts
#entschieden werden, welcher Steuersatz zur Anwendung kommt. Die Ausgabe kann
#zum Beispiel wie folgt aussehen:
#Geben Sie Ihr Gehalt in Euro ein:
#3000
#Es ergibt sich eine Steuer von 660.0 Euro
#oder sie kann so aussehen:
#Geben Sie Ihr Gehalt in Euro ein:
#2000
#Es ergibt sich eine Steuer von 360.0 Euro

eingabe = float(input("Geben Sie Ihr Gehalt in Euro ein: "))
steuer1 = 0.22
steuer2 = 0.18

if eingabe > 0 and eingabe <= 2500:
    print(f"Es ergibt sich eine Steuer von {(eingabe * steuer2):.2f}€")
elif eingabe > 2500:
    print(f"Es ergibt sich eine Steuer von {(eingabe * steuer1):.2f}€")
else:
    print("Sie haben eine negative Wert eingegeben")