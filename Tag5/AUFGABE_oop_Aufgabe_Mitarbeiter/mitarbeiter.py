from projekt import Projekt
# projekte = []


class Mitarbeiter:

    def __init__(self, name, pos):
        self.name = name
        self.position = pos
        self.projekte = []

    def projekt_hinzufuegen(self, projekt):
        if isinstance(projekt, Projekt):
            self.projekte.append(projekt)
            print(
                f"Projekt {projekt.name} - {projekt.status} wurde zu {self.name} hinzugefügt")
        else:
            print("Fehler! Es würde kein Projekt-Objekt übergeben")

        # allen Projekten zufügen
        # if projekte.count(self.name):
        #     projekte.append(prname)

    def projekt_status_aendern(self, projekt_name, neuer_status):
        for projekt in self.projekte:
            if projekt.name == projekt_name:
                projekt.status_aendern(neuer_status)
                print(
                    f"Status vom Projekt {projekt_name} zu {neuer_status} geändert")
            else:
                print(f"Projekt {projekt_name} nicht gefunden")

    def projekte_anzeigen(self):
        print(f"Projekte von {self.name}:")
        print(self.projekte)
        print()

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Projekte: {self.projekte}"


# def alle_projekte_anzeigen():
#     print("Alle Projekte")
#     print(projekte)
