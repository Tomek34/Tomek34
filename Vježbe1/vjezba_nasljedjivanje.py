class Osoba:

    def __init__(self, ime, prezime, oib):
        self.ime = ime
        self.prezime = prezime
        self.oib = oib

    def ispis(self):
        print(f"{self.ime}, {self.prezime}")
        print(f'OIB {self.oib}')
        print()

pero = Osoba("Pero", "Perić", "12345678911")
pero.ispis()


class Zaposlenik(Osoba):

    def __init__(self, ime, prezime, oib, ime_tvrtke):
        super().__init__(ime, prezime, oib)
        self.ime_tvrtke = ime_tvrtke

    def ispisi_podatke_o_zaposleniku(self):
        super().ispis()
        print(f'Zaposlen u: {self.ime_tvrtke}.')   

    """def ispis(self):
        # ovaj ispis zamjenjuje ispis klase Osoba
        print(f"{self.ime}, {self.prezime}")
        print(f'OIB {self.oib}')
        print(f'Zaposlen u {self.ime_tvrtke}')
        print()"""

stipe = Zaposlenik("Stipe", "Stipić", "01", "Kamenolom d.o.o.")
stipe.ispis()
stipe.ispisi_podatke_o_zaposleniku


pero = Zaposlenik(pero.ime, pero.prezime, pero.oib, "Pero j.d.o.o.")
pero.ispisi_podatke_o_zaposleniku
print()
pero.ime = "Ante"
pero.ispis()

# ZADATAK: definirati klasu Umirovljenik koja ima sve što ima i klasa Osoba
# uz dodataka medote isois_penzije koja će ispisati:
# "Penzija je mala, moraš natrag na posao"

class Umirovljenik(Osoba):

    def ispis_penzije(self):
        print("Penzija je mala, moraš natrag na posao.")

dida = Umirovljenik("Stipe", "Stipić", "000")
dida.ispis()
dida.ispis_penzije()