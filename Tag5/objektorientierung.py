# Mit der Objektorientierung (OOP) hat man zusätzliche Möglichkeiten, den Programmaufbau und Struktur
# des Codes mit Klassen, Objekten, Eigenschaften und Vererbung verbessern
# Klassen gruppieren Dinge aus dem echten Leben, sind eine Art Bauplan / Blaupause
# Aus Klassen können einzigartige Objekte erstellt werden
# Alle Eigenschaften und Methoden Klasse nennt man auch "Member"

class Fahrzeug:
    geschwindigkeit = 0

# self ist eine Selbstreferenz auf das Objekt selbst
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert

    def ausgabe(self):
        print("Geschwindigkeit: ", self.geschwindigkeit)


opel = Fahrzeug()
opel.ausgabe()
opel.beschleunigen(20)
opel.ausgabe()

volvo = Fahrzeug()
volvo.beschleunigen(15)
volvo.ausgabe()

# Encapsualtion (Kapselung) in Python
# Sichtbarkeiten von Eigenschaften und Methoden werden meist in objektorieren Programmiersprachen
# über die Keywords public, protected und private geklärt
# Man verwendet den "_" bei den Eigenschaften um anzudeuten, dass diese Variable nicht direkt
# verändert soll und, wenn es benötigt mit _ (doppelter Unterstrich) kann man es quasi unsichtbar für
# andere machen. Es gibt keine komplette Encapsulation in Python


