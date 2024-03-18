# Zeichenketten sind Objekte des Typs 'str'
# Können in einfache, doppelte oder dreichach Hochkommate gesetzt werden

tx = "Das"
print("Text:", tx)
print("Typ:", type(tx))

# mit len(meinString) kann man die Anzahl der Zeichen in einem String erfahren
print("Anzahl der Zeichen:", len(tx))

for z in tx:
    print(z)

for i in range(0,len(tx),2):
    print(f"{i}: {tx[i]}")
    
tx = 'Auch das ist eine Zeichenkette'
print(tx)

tx = """Diese Zeichenkette
        steht in
        mehreren Zeilen"""

print(tx)


tx = 'Hier sind "doppelte Hochkommata" gespeichert'

print("\n")

# Auf Strings können, wie bekannt zum Verketten (Konkatenieren) der + Operator angewendet werden
# Aber auch das * Stern - Zeichen hat eine Funktion, sie kann ein String häufiger ausgeben
# Strings (Zeichenketten) sind nicht veränderbar (immutable), wenn Sie also Funktionen auf Zeichenketten anwenden, wo der
# Originalstring verändert soll, muss dieser überschrieben werden mit der Rückgabe Funktion

kreis = "-oooo-"
stern = "***"
linie = stern + kreis * 3 + stern
print(linie)


# Slices (Stubstrings, Teilzeichenketten)
# Ein Slice wird mit der Angabe einer eckigen Klammer angegeben
# Der erste Parameter gibt den Startindex an, der zweite Parameter den exklusvien Endindex, ein optionaler dritter die Schrittweite

tx = "Hallo"
print("Text:", tx)

print("[1-4]:", tx[1:4])
print("[:4]:", tx[:4])
print("[2:]:", tx[2:])
print("[:]:", tx[:])
print("[1]:", tx[1])
print("[1:-2]:", tx[1:-2])
print("[::-1]:", tx[::-1])
print("[::-2]:", tx[::-2])

tx = "Das ist ein Beispielsatz"
print("Text:", tx)

such = "ei"
print("Suchtext:", such)
print()

# zählt die Anzahl der Vorkommen eines Suchtextes innerhalb eines analysierten Textes
anz = tx.count(such)
print(f"count: Der String {such} kommt {anz} mal vor")
print()

#find() liefert index-Position, an der ein Suchtext innerhalb eines analysierten Textes vorkommt
#gibt -1 zurück, der Suchtext nicht vorkommt
pos = tx.find(such)
if pos != -1:
    print("find: an Position:", pos)

#rfind() liefer die letzte Position eines Suchtextes    
pos = tx.rfind(such)
if pos != -1:
    print("rfind: Zum letzten mal an Position", pos)
    print()
    
#mit startswith und endswith() kontrolliert man, ob ein Text mit einer bestimmten Zeichenkette beginnt, oder endet
if tx.startswith("Das"):
    print("Text beginnt mit Das")

if not tx.endswith("Das"):
    print("Text beginnt nicht mit Das")
  
#replace ersetzt gesuchten Teilstring durch einen anderen und liefert den geänderten Text zurück
#Achtung: Der Originalstring kann nicht verändert werden! (Originalstring überschreiben, wenn gewollt)
tx = "Das ist ein Beispielsatz"
tx = tx.replace("ist", "war")
print(tx)

z = 48.2
tx = str(z)
tx = tx.replace(".",",")
print("Zahl mit Komma:", tx)

print()
# isdigit() überprüft, ob übergebenes Zeichen eine Zahl ist
tx = "1112312gfsdfsd1242"
for zeichen in tx:
    if zeichen.isdigit():
        print(f"Zeichen: {zeichen} ist eine Zahl")
    else:
        print(f"Zeichen: {zeichen} ist keine Zahl")

print()

# isalpha() überprüft, ob übergebens Zeichen ein Buchstabe ist
for zeichen in tx:
    if zeichen.isalpha():
        print(f"Zeichen: {zeichen} ist ein Buchstabe")
    else:
        print(f"Zeichen: {zeichen} ist kein Buchstabe")

# mit lower() werden Buchstaben klein geschrieben und mit upper() alle groß
tx = "hAlLo WelT"
print(tx.lower())
print(tx.upper())

# whitespace (also Leerzeichen, Tabs, Zeilenumbrüche) entfernen wir mit strip()
tx = "    \t Hallo Welt     \n\t"
print(f"|{tx}|")
print(f"|{tx.strip()}|")


tx = "Das ist ein Satz"
print("Text", tx)

wortliste = tx.split()

for i in range(0, len(wortliste)):
    print("Element:", i, wortliste[i])
    
print()

tx = "Maier;Hans;67141;3500,00;15.03.62"
print("Text:", tx)
wortliste = tx.split(";")

for i in range(0, len(wortliste)):
    print("Element:", i, wortliste[i])
