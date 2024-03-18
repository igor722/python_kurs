# Stringverkettung

text = "Halo" + " " + "Welt"

print(text)

value = 20
print("Wert beträgt:", value)

a = 23
b = 7.5
c = a + b
print("Ergebnis: ", end="")
print(a, "+", b, "=", c, sep=" ")

#print mit .format() u.a. die Ausgabe formatieren ABER auch Platzhalter
a = 23.5845565896
b = 5.4545565
print("Ausgabe der Variablen a: {} und b: {}".format(a,b))
print("Ausgabe der Variablen a: {:.2f} und b: {:.2f}".format(a,b))

#formatierte Ausgabe mit formatiertem-String-Literal
text = f"Ausgabe der Variablen a: {a:5.2f} und b: {b:5.2f}"
print(text)