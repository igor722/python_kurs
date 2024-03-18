# Auch als Switch case gennant
import random

# x = input('Bitte ein Stadt eingeben: ')
x = "Paris"
match(x):
    case 'Paris':
        print('Frankreich')
    case 'Rom':
        print('Italien')
    case 'Madrid':
        print('Spanien')
    case _:
        print('Unbekantes Land')


x = random.randint(1, 6)
print("x =", x)
match(x):
    case 1 | 3 | 5:
        print("Ungerade Zahl")
    case 2 | 4 | 6:
        print("Gerade Zahl")
    case _:
        print("Kein Würfelwert")


x = random.randint(1, 10)
print("x2 =", x)
match x * 1.5:
    case x if x < 5:
        print("kleiner Wert")
    case x if x > 5:
        print("größer Wert")
