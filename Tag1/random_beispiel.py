import random
random.seed()

a = random.randint(1, 10)
b = random.randint(1, 10)

print(f"Die aufgabe ist: {a} + {b}")

eingabe = int(input("Bitte Lösungsvorschlag eingeben: "))

print(f"Ihre Antwort: {eingabe}")
print(f"Richtige Antwort: {a + b}")

if a + b == eingabe:
    print("Richtig!")
else:
    print("Falsch!")