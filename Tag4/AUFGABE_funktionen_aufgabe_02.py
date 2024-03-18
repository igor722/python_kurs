# Schreiben Sie eine Python-Funktion bewerte_zahlenfolge, die drei ganze Zahlen a, b und c als
# Parameter entgegennimmt. Die Funktion soll überprüfen, ob diese Zahlen in aufsteigender, ab-
# steigender oder in keiner spezifischen Reihenfolge angeordnet sind. Die Funktion gibt einen von
# drei möglichen Strings aus: "aufsteigend", "absteigend" oder "keine spezifische Rei-
# henfolge". Rufen Sie die Funktion jeweils mit einem Beispiel für die drei Möglichkeiten ein:
# bewerte_zahlenfolge(1,2,3) #Gibt aufsteigend aus
# bewerte_zahlenfolge(3,2,1) #Gibt absteigend aus
# bewerte_zahlenfolge(1,3,2) #keine spezifische Reihenfolge

def bewerte_zahlenfolge(a, b, c):
    if a < b < c:
        print(f"Zahlen: {a}, {b}, {c} gibt aufsteigend aus")
    elif c < b < a:
        print(f"Zahlen: {a}, {b}, {c} gibt absteigend aus")
    else:
        print(f"Zahlen: {a}, {b}, {c} keine spezifische Reihenfolge")


bewerte_zahlenfolge(2, 8, 52)
bewerte_zahlenfolge(10, 9, 6)
bewerte_zahlenfolge(45, 8, 52)
