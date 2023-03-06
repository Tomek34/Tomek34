class RezultatMjerenja:
    def __init__(self, vrijednost, mjerna_jedinica, tip) -> None:
        self.vrijednost = vrijednost
        self.mjerna_jedinica = mjerna_jedinica
        self.tip = tip

def lijepi_ispis(self):
    print(f"Vrijednost {self.tip} mjerenja je {self.vrijednost}{self.mjerna_jedinica}")    
    
    # ZADATAK:
    # napraviti metou u ovoj klasi koja prima objekt koje je instanca ove klase i
    # vraća True ako je:
    # - objekt istog tipa kao i objekt koji smo primili kao argument klase
    # - vrijednost oba objekta ista
    # u svim ostalim slučajevima vraća False

    # odnosno radi kao i ovo na linijama 22 i 23


rez_1 = RezultatMjerenja(100, '°C', "TEMPERATURA")
rez_2 = RezultatMjerenja(90, '°C', "TEMPERATURA")
rez_3 = RezultatMjerenja(90, '°C', "TEMPERATURA")
rez_4 = RezultatMjerenja(90, 'hPa', "TLAK")

if rez_1.tip == rez_2.tip:
    print(rez_1.vrijednost == rez_2.vrijednost)