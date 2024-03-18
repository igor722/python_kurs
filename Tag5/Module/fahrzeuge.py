class Fahrzeug:

    def __init__(self, bez='leer', ge=0):
        self.bezeichnung = bez
        self.geschwindigkeit = ge

    def __str__(self):
        return f"{self.bezeichnung} {self.geschwindigkeit}km/h"

    #def __del__(self):
        #print(f"Entfernt {self}")

    # self ist eine Selbstreferenz auf das Objekt selbst
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert

    def ausgabe(self):
        print("Geschwindigkeit: ", self.geschwindigkeit)


class PKW(Fahrzeug):
    def __init__(self, bez, ge, ins):
        super().__init__(bez, ge)
        self.insassen = ins

    def __str__(self):
        return f"{super().__str__()} {self.insassen} Insassen"

    def einsteigen(self, anzahl):
        self.insassen += anzahl

    def aussteigen(self, anzahl):
        self.insassen -= anzahl
