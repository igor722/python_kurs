# Erstelle ein Programm, das eine Liste von Wörtern vom Anwender einliest. Das Programm soll so lange
# beim Anwender nach Wörtern fragen, bis er mit dem Wort „abbruch“ den Einlesevorgang beendet. Das
# Programm soll dann jedes Wort in der Liste umkehren (also rückwärts schreiben) und die umgekehrten
# Wörter in einer neuen Liste speichern. Anschließend soll die neue Liste alphabetisch sortiert ausgegeben
# werden.
# Beispiel:
# Eingabe: ["Hallo", "Welt", "Python"]
# Ausgabe: ['nohtyP', 'ollaH', 'tleW'] (nach dem Sortieren)
# Hinweise:
# Verwende Slicing, um die Wörter umzukehren.

abbruch = False
woerter = []

while abbruch != True:
    wort = input(
        "Bitte Wort ins Liste zufügen\num Programm zu schliessen tippen Sie \"abbruch\" ein\n")
    if wort.lower() == "abbruch":
        abbruch = True
    else:
        woerter.insert(0, wort[::-1])

woerter.sort()
print(woerter)
