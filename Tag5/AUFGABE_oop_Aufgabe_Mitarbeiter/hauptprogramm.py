import mitarbeiter
from mitarbeiter import Mitarbeiter
from projekt import Projekt


def main():
    mb1 = Mitarbeiter("Max", "HR")

    p1 = Projekt("Website-Relaunch", "Überarbeitung der Unternehmens Webseite")

    mb1.projekt_hinzufuegen(p1)

    mb1.projekte_anzeigen()

    mb1.projekt_status_aendern("Website-Relaunch", "In Arbeit")
    
main()

# mb2 = Mitarbeiter("Mark", "IT")
# mb3 = Mitarbeiter("Anna", "CEO")
# mb4 = Mitarbeiter("Emma", "Marketing")
# mb5 = Mitarbeiter("Lucy", "K1")

# mb1.projekt_hinzufuegen("Projekt P4")
# mb1.projekt_hinzufuegen("Projekt P3")
# mb1.projekt_hinzufuegen("Projekt P5")
# mb1.projekt_hinzufuegen("Projekt P6")
# mb3.projekt_hinzufuegen("Projekt P1")
# mb2.projekt_hinzufuegen("Projekt P2")

# mb1.projekte_anzeigen()
# mb3.projekte_anzeigen()
# mb2.projekte_anzeigen()

# mitarbeiter.alle_projekte_anzeigen()

# print(mb1)
