# Eine Sequenz von Objekten in ihrer allgemeinsten Form
# Kann Elemente unterschiedlicher Datentypen enthalten
# Eine Liste veränderbar (mutable), im Gegensatz zu den unveränderlichen (immutable) Strings
# Im Prinzip ist ein String nichts anderes als eine Liste zur Speicherung von einzelnen Zeichen
import random

z = [3, 6.2, -12]
print("Liste: ", z)
print("Element: ", z[0])
print("Slice: ", z[:2])

print("Schleife: ")
for element in z:
    print(element)

print("Schleife mit Intex: ")
for i in range(len(z)):
    print(f"{i}: {z[i]}")

# random.choice(liste) für zufallige Auswahl
print("Zufälliges Element: ", random.choice(z))

# random.shuffle(liste) mischt die Liste
random.shuffle(z)
print("Nach dem Mischen: ", z)


# Mehrdimensionale Listen
# Eine Liste kann unterschiedliche Datentypen enthalten, deshalb können Elemente in einer Liste wieder eine Liste sein
# Sie bilden dadurch mehrdimensionale Listen

z = [["Paris", "Fr", 3.5], ["Rom", "It", 4.2], ["Madrid", "Sp", 3.2]]
print("Mehrdimensionale Liste: ", z)
print("Länge: ", len(z))

print("Unter-Liste: ", z[0])
print("Länge der Erste Unterliste: ", len(z[0]))
print("Slice von Unterlisten: ", z[:2])
print()
print("Element: ", z[2][0])
print("Länge der String Madrid: ", len(z[2][0]))
print("Länge der String Madrid: ", len(z[2][0]))
print("Slice von Elementen: ", z[2][0][:3])

for i in range(len(z)):
    print(f"{i}: {z[i][0]} hat {z[i][2]} Mio. Einwohner")

for stadt in z:
    print(f"{stadt[0]} hat {stadt[2]} Mio. Einwohner")

# Nützliche Methoden auf Listen

z = ["Paris", "Lyon", "Metz"]
print("Liste: ", z)

z.insert(1, "Nantes")
print("Liste: ", z)

z.sort()
print("Sortieren: ", z)

z.reverse()
print("Umdrehen: ", z)

such = "Metz"
if such in z:
    z.remove(such)
    print("Entfernt: ", z)

z.append("Paris")
print("Fügt am Ende hinzu: ", z)

such = "Paris"
print("Anzahl gefunden: ", z.count(such))

print()
print()
# Dictionaries
# Dictonaries sind assoziative Listen, ähnlich einem Wörterbuch
# Ein einzelnes Element stellt ein Schlüssel-Wert Paar dar (key-value-pair)
# Dictionsaries sind verlanderliche Objekte
# Über den Schlüssel greift man auf Wert zu, so wie bei einer normalen Liste über den Index auf der Wert zugegriffen werden kann

dc = {"Peter": 31, "Julia": 28, "Werner": 35}
print("Dictionary:", dc)
print("Dictionary länge: ", len(dc))

dc_vergleich = {"Peter": 31, "Werner": 35, "Julia": 28}

if dc == dc_vergleich:
    print("Gleich")

dc["Julia"] = 27
print("Wert ersetzt: ", dc)

# Wenn Element nicht vorhanden, neu anlegen
dc["Moritz"] = 22
print("Element in der Liste zugefügt: ", dc)

if "Julia" in dc:
    print(dc["Julia"])

del dc["Julia"]
if "Julia" not in dc:
    print("Nicht enthalten")
print("Element entfernt: ", dc)

# Views / Methoden
# keys() erstellt einer Liste mid den Schlüsseln
k = dc.keys()
print("Schlussel: ", k)

# values() erstellt einer Liste mit Werten den Dictionaries
v = dc.values()
print("Werte: ", v)

# items() erstellt einer Liste mit Keys/Values als Tupel
i = dc.items()
print("Items: ", i)