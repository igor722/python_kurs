# Aufgabe 03
# Du bist für die Verwaltung einer kleinen Bibliothek verantwortlich und hast eine Liste von Bü-
# chern, die nach Titel und Kategorie geordnet werden sollen. Erstelle hierfür ein Skript mit dem
# Namen „buecher_kategorisieren.py“. Die Informationen zu jedem Buch sind in einem speziellen
# Format gegeben: "Titel:Kategorie". Deine Aufgabe ist es, ein Programm zu schreiben, das diese
# Liste verarbeitet und jedes Buch nach seinem Titel und seiner Kategorie organisiert.
# Anforderungen:
# 1. Verwende die gegebene Liste von Büchern. Jeder Eintrag in der Liste ist ein String, der
# ein Buch repräsentiert, formatiert als "Titel:Kategorie".
# 2. Schreibe ein Programm, das diese Liste durchläuft und für jedes Buch den Titel und die
# Kategorie extrahiert.
# 3. Benutze die Methode split(':'), um die Strings zu trennen und Zugriff auf den Titel
# und die Kategorie zu bekommen.
# 4. Drucke die Informationen jedes Buches in einem schönen Format aus, zum Beispiel: "Ti￾tel: [Buchtitel], Kategorie: [Buchkategorie]".
# Hinweis:
# Denke daran, dass die split-Methode eine Liste zurückgibt, aus der du die Teile extrahieren kannst, die du
# benötigst.
# Bücherliste: Python Grundlagen:Programmieren, Einführung in SQL:Datenbanken' Der
# Pragmatische Programmierer:Entwicklung,
# Algorithmen Einführung:Computerwissenschaft, Moby Dick:Roman, Einführung in
# Python:Sachbuch, Krieg und Frieden:Roman, Python Kochbuch:Sachbuch

liste_buecher = []
eingabe_fertig = False

while not eingabe_fertig:
    buch_eingabe = input(
        "Bitte eine neue Buch eintragen in Format \"Titel:kategorie\"\nWenn Sie fertig sind, bitte \"x\" eingeben\n")
    if buch_eingabe == "x":
        eingabe_fertig = True
    else:
        buch = buch_eingabe.split(":")
        liste_buecher.append([buch[0], buch[1]])

liste_buecher.sort()
print("Bücher in Bücherei:")
for buch in liste_buecher:
    print(f"Titel: \"{buch[0]}\", Kategorie: \"{buch[1]}\"")
