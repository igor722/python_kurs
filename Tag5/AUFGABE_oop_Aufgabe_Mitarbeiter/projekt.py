class Projekt:

    def __init__(self, name, beschreibung, status='Nicht gestartet'):
        self.name = name
        self.beschreibung = beschreibung
        self.status = status

    def status_aendern(self, neuer_status):
        self.status = neuer_status
        print(
            f"Neuer Status der {self.name} ist: {self.status}")
