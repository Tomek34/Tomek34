class RezultatMjerenja:
    def __init__(self, vrijednost, mjerna_jedinica, tip) -> None:
        self.vrijednost = vrijednost
        self.mjerna_jedinica = mjerna_jedinica
        self.tip = tip

rez_1 = RezultatMjerenja(100, '°C', "TEMPERATURA")
rez_2 = RezultatMjerenja(90, '°C', "TEMPERATURA")

if rez_1.tip == rez_2.tip:
    print(rez_1.vrijednost == rez_2.vrijednost)