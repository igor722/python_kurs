# Besondere Member in Python
# Es gibt besondere Member, die häufig im Zusammenhang mit Klassen definiert werden
# Leicht erkenbar am doppelten "__davor" und "danach__"
# __init__() = Kontruktor, bereitet das Objekt für die Nutzung vor
# __str__() = stellt Eigenschaften als Key_value Pair dar
# __del__() = entfernt Objekt am Ende seiner Lebensdauer (wenn es also in der Regel nicht mehr benötigt wird)

class Fahrzeug:

    def __init__(self, bez='leer', ge=0):
        self.bezeichnung = bez
        self.geschwindigkeit = ge

    def __str__(self):
        return f"{self.bezeichnung} {self.geschwindigkeit}km/h"

    def __del__(self):
        print(f"Entfernt {self}")

    # self ist eine Selbstreferenz auf das Objekt selbst
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert

    def ausgabe(self):
        print("Geschwindigkeit: ", self.geschwindigkeit)


audi = Fahrzeug(bez="R8", ge=320)
mercedes = Fahrzeug(bez="SLK", ge=220)
geilere_mercedes = Fahrzeug(bez="AMG-GT", ge=320)
porsche = Fahrzeug(bez="911 GT3 RS", ge=300)
porsche.geschwindigkeit = 350
porsche.bezeichnung = "Superkrasser 911 GT3 RS"


audi.ausgabe()

print(audi)
print(audi.__dict__)
print(mercedes)
print(geilere_mercedes)
print(porsche.__dict__)
