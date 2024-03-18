# Operatormethoden werden für Objekte mithilfe von Operatoren aufgerufen
# Bei vordefinierten Datentypen sind diese bereits vorhanden
# Für unsere eigenen Klassen (unser eigenen Datentypen) können wir diese selbst definieren
# Potentiell vorhanden Vergleichsoperatoren sind: __gt__(), __lt__(), __eq__(), __ge()__, __le__(), __ne__()
# Mathematische Operatoren: __add__(), __sub__(), __mul__(), __truediv__(), __floordiv__(), __mod__, __pow__

class Fahrzeug:

    def __init__(self, bez='leer', ge=0):
        self.bezeichnung = bez
        self.geschwindigkeit = ge

    def __gt__(self, other):
        return self.geschwindigkeit > other.geschwindigkeit

    def __eq__(self, other):
        return self.geschwindigkeit == other.geschwindigkeit and self.bezeichnung == other.bezeichnung

    def __sub__(self, other):
        return self.geschwindigkeit - other.geschwindigkeit


opel = Fahrzeug("Opel Admiral", 60)
volvo = Fahrzeug("Volvo Amazon", 45)

if opel > volvo:
    print("Opel ist schneller")
elif opel == volvo:
    print("Beide sind gleich")
else:
    print("Beide sind nicht gleich")

different = opel - volvo
print(f"Geschwindigkeitsdifferenz: {different} km/h")
