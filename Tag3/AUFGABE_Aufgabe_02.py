satz = "Satz indem das längste Wort gesucht wird: Dies ist ein Beispielsatz"

def finde_laengstes_wort():
    woerter = satz.split()
    print(f"Laengstes Wort ist: \"{max(woerter, key=len)}\"")

finde_laengstes_wort()