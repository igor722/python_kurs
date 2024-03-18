sonderzeichen = '^°"§$%&/()=@€~?`/*-+,\\\"\'[]#;:-_.<>|'
kennwort = input("Bitte Kennwort eingeben: ").strip()

#print(kennwort)

if len(kennwort) < 8:
    print("Kennwort zu kurz")
else:
    if any(char.isdigit() for char in kennwort):
        if any(char.isalpha() for char in kennwort):
            if any(char in sonderzeichen for char in kennwort):
                if any(char.isupper() for char in kennwort):
                    if any(char.islower() for char in kennwort):
                        print("Kennwort ist in Ordnung")
                    else:
                        print("Fehlt mindestens eine Kleinbuchstabe")
                else:
                    print("Fehlt mindestens eine Großbuchstabe")
            else:
                print("Fehlt mindestens eine Sonderzeichen")
        else:
            print("Fehlt mindestens eine Buchstabe")
    else:
        print("Fehlt mindestens ein Zahl")
