for zahl in 8, 3, 7:
    print(f"Zahl: {zahl}, Quadrat: {zahl * zahl}")

for stadt in "Paris", "Rom", "Madrid":
    print(f"Stadt: {stadt}")

for zeichen in "Rom":
    print(f"Zeichen: {zeichen}")

for name in ["Jens", "Mohammad", "Nikki"]:
    print(f"Namen: {name}")

# in => Membership Operator (Zugehörigkeit Operator)
fruechte = ["Apfel", "Banane", "Kirsche"]
ist_enthalten = "Banane" in fruechte
print(ist_enthalten)

nachricht = "Hallo, Welt!"
wort_ist_enthalten = "Welt" in nachricht
print(wort_ist_enthalten)

farben = ["Rot", "Grün", "Blau"]
farbe = "Rot"
if farbe in farben:
    print(f"{farbe} ist in Farben enthalten")
else:
    print(f"{farbe} ist nicht in Farben enthalten")

# neben in gibt es auch noch "not in", das wahr wird, wenn der Wert nicht in einem iterierbaren Objekt ist
# Ein iterierbares Objekt, ist ein Art Sammlung mit Elementen, wo jedes Element abgefragt wird

# Schleifeabbruch mit break
for i in 12, -4, 7:
    if i*i > 200:
        break
    print(f"Zahl: {i}, Quadrat: {i*i}")

# Schleifendurchlauf überspringen mit continue
for zahl in 1, 2, 3, 4, 5, 6, 7, 8, 9:
    if zahl % 2 == 0:
        continue
    print(zahl)

# Verschachtelte Kontrollstruktur
for x in -2, -1, 0, 1, 2:
    if x > 0:
        print("positiv")
    else:
        if x < 0:
            print("negativ")
        else:
            print("0")

# range() Funktion hat 3 Übergabeparameter
# 1. Startindex
# 2. Endindex
# 3. Schrittweite
print("For Schleife mit 3 Parameter")
for i in range(3, 11, 2):
    print(f"Zahl: {i}, Quadrat: {i*i}")

# mit zwei Parameter ist die Schrittweite optional
print("For Schleife mit 2 Parameter")
for i in range(5, 9):
    print(f"Zahl: {i}")

# bei range mit einem Parameter, fällt Startindex weg
print("For Schleife mit 1 Parameter")
for i in range(3):
    print(f"Zahl: {i}")
# Foreach ähnlich wie normale for Schleife mit Startindex 0, Endindex ist Ende der Liste un Schrittweite 1
