# Aufgabe 03
# Schreiben Sie eine Python-Funktion konvertiere_temperatur, die zwei Parameter entgegen-
# nimmt: den Temperaturwert temperatur (ein Float- oder Ganzzahlwert) und die Einheit einheit
# (ein String, der entweder "C" für Celsius oder "F" für Fahrenheit sein kann). Die Funktion soll die
# Temperatur von Celsius in Fahrenheit umrechnen, wenn einheit "C" ist, und von Fahrenheit in
# Celsius, wenn einheit "F" ist. Recherchieren Sie die Berechnung von Celsius in Fahrenheit und
# Fahrenheit in Celsius selbständig im Internet. Die umgerechnete Temperatur soll als String zu-
# rückgeben werden, der auf zwei Nachkommastellen begrenzt wurde.
# Beispielaufrufe der Funktion konvertiere_temperatur:
# konvertiere_temperatur(100, "C")
# # Sollte 212.0 ausgeben da 100°C = 212°F
# konvertiere_temperatur(32, "F")
# # Sollte 0.0 ausgeben da 32°F = 0°F

def konvertiere_temperatur(wert, einheit):
    if einheit.lower() == "c":
        celsius = wert
        fahrenheit = celsius * 9/5 + 32
        print(f"{celsius}C° beträgt {fahrenheit}°F")
        # F = C * 9/5 + 32
    elif einheit.lower() == "f":
        fahrenheit = wert
        #°C = (°F - 32) * 5/9
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F beträgt {celsius}C°")
    else:
        print("Fehler bei Eingabe")

konvertiere_temperatur(100, "c")
konvertiere_temperatur(32, "f")
