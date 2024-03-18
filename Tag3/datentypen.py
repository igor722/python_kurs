# Python kann bei Zahlen diese sehr einfach in unterschiedliche Basen konvertieren:

print("=====================ZAHLENTYPEN=====================")
a = 27
print("Dezimal.", a)
print("Hexadezimal.", hex(a))
print("Oktal:", oct(a))
print("Dual:", bin(a))

print()
b = 0x1a + 12 + 0b101 + 0o67
print("Summe:", hex(b))

# Häufig kann es nützlich sein, den Typ einer Variablen zu kennen mi der type() Funktion
print("=====================TYPE=====================")
a = 2
print("Typ:", type(a))
b = 12 / 6
print("Typ:", type(b))
c = 12 // 6
print("Typ:", type(c))
d = 12 % 6 == 0
print("Typ:", type(d))
