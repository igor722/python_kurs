# import fahrzeuge
from fahrzeuge import PKW, Fahrzeug


def main():

    fiat = PKW("Fiat Marea", 50, 0)
    fiat.einsteigen(3)
    fiat.aussteigen(1)
    fiat.beschleunigen(30)
    print(fiat)

    audi = Fahrzeug("R8", 300)
    audi.beschleunigen(20)
    print(audi)


main()
