import random
random.seed()

a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b

print(f"Die Aufgabe: {a} + {b}")

for i in 1, 2, 3, 4:
    zahl = int(input("Bitte Lösungsvorschlag eingeben: "))
    if zahl == c:
        print(zahl, " ist richtig!")
        break
    else:
        print("Zahl ist falsch!")
