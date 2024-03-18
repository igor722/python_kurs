# Aufgabe 02
# Schreibe ein Python-Programm, das es dem Anwender ermöglicht, einen beliebigen Text einzugeben. Das
# Programm soll daraufhin alle einzigartigen Buchstaben im Text zählen und die Anzahl ihres Auftretens er￾mitteln. Die Ausgabe soll in Form eines Dictionaries erfolgen, wobei jeder Buchstabe der Schlüssel ist und
# die Anzahl seines Vorkommens der zugehörige Wert. Groß- und Kleinschreibung sollen dabei nicht unter￾schieden werden, und Leerzeichen sollen nicht gezählt werden.
# Hinweise:
#  Leerzeichen im Text sollen bei der Zählung ignoriert werden. Nutze replace() um Leerzeichen zu
# entfernen.
#  Speichere die Ergebnisse in einem Dictionary, wobei jeder einzigartige Buchstabe ein Schlüssel ist
# und die Anzahl seines Vorkommens der Wert.

buchstaben = {}

print("Buchstabenzähler")
text = input("Bitte ein Text eingeben:\n")
text = text.lower().replace(" ", "")

for i in range(len(text)):
    buchstaben[text[i]] = text.count(text[i])

print(buchstaben)
