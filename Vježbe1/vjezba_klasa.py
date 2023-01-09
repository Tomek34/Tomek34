class Racun:
    """Ova klasa definira sve potrebno kako bi radili s racunima"""
    
    def __init__(self, broj_racuna, datum_izdavanja, stavke):
        self.broj_racuna = broj_racuna
        self.datum_izdavanj= datum_izdavanja
        self.stavke = stavke
        self.iznos_pdv = 0.0
        self.ukupan_iznos = 0.0

    def ispis_racuna(self):
        print(f'Broj racuna {self.broj_racuna}')
        print(f'Datum izdavanja: {self.datum_izdavanj}')
        print()
        print("Stavke racuna")

        print('\t')


racun = Racun(1, '05.01.2023.', [])
racun.ispis_racuna()

