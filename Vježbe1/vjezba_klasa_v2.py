from ast import arg

class Stavka:
    def __init__(self, proizvod, cijena, kolicina):
        self.proizvod = proizvod
        self.cijena = cijena
        self.kolicina = kolicina

    def iznos(self):
        return self.cijena*self.kolicina

    def ispis(self):
        print(f'\t{self.proizvod}\t\t{self.cijena}\t\t{self.kolicina}')

class Racun:
    """Ova klasa definira sve potrebno kako bi radili s racunima"""
    
    def __init__(self, broj_racuna, datum_izdavanja, stavke = None):
        """
        broj_racuna, datum_izdavanja s obavezni argumenti
        stavke su OPCIONALNI ARGUMENT
        ako se ne pošalju, biti će prazna lista
        """
        self.broj_racuna = broj_racuna
        self.datum_izdavanja= datum_izdavanja
        self.stavke = []
        #ako je korisnik unio stavke, uzmi tu vrijednost
        if stavke:
            for stavka in stavke:
                self.dodavanje_stavke(stavka)

        
        self.iznos_pdv = 0.0
        self.ukupan_iznos = 0.0

    def ispis_racuna(self):
        print(f'Broj racuna {self.broj_racuna}')
        print(f'Datum izdavanja: {self.datum_izdavanja}')
        print()
        print(f'Stavke racuna:')
        print('\tProizvod\tCijena\tKolicina')
        print('-'*50)
        for stavka in self.stavke:
            stavka.ispis()
        print()
        self.izracunaj_ukupni_iznos()
        print(f'Ukupan iznos: {self.ukupan_iznos} €')

#zadatak: napisati metodu u klasi Racun za dodavanje stavke
#pretposatvke: stavka se sastoji od imena prozivoda i cijene
#stavku spremiti u listu stavki {self.stavke} kao što smo to radili u prethodnom primjeru
    def dodavanje_stavke(self, stavka):
        self.stavke.append(stavka)

    def izracunaj_ukupni_iznos(self):
        self.ukupan_iznos = 0
        for stavka in self.stavke:
            self.ukupan_iznos += stavka.iznos()

#primjer nakon dodavanja dvije stavke:
"""
self.stavke = [
    {'proizvod': 'Mlijeko', 'cijena':2.0, 'kolicina' : 2},
    {'proizvod': 'Kruh', 'cijena':2.0, 'kolicina': 1}]"""

stavka = Stavka('Mlijeko', 1.75, 2)
racun = Racun(
    1, 
    '05.01.2023',
    stavke = [stavka]
)
racun.ispis_racuna()
racun.dodavanje_stavke(Stavka('Salama', 1.45, 1))
racun.ispis_racuna()
racun.dodavanje_stavke(Stavka('Papir', 4.00, 3))
racun.ispis_racuna()

"""
racun = Racun(1, '05.01.2023.', {'Mlijeko', 2.0})
racun.ispis_racuna()

racun_2 = Racun(2, '04.01.2023.', ['Kruh', 1.50])
racun_2.ispis_racuna()

racun_3 = Racun(3, '03.01.2023.', [])
racun_3.ispis_racuna()
racun_3.dodavanje_stavke()
"""





        