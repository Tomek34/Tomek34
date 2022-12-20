vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'TAM', 'ST 001 ZZ', 2013, 97000.00],
    6 : ['Kombi', 'FAP', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'FAP', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'FAP', 'ZG 002 ZZ', 2010, 9300.00]
}

def ispis_zaglavlja_tablice():...

def ispisi_tijelo_tablice(tip_vozila):
    for kljuc, vrijednost in vozni_park.items():
        if vrijednost[0] != tip_vozila:
            continue
        print(f'{kljuc}', end='\t')
        for element in vrijednost:
            if type(element) == str:
                if len(element) > 9:
                    print(f'{element}', end='\t')
                else:
                    print(f'{element}', end='\t\t')
            else:
                print(f'{element}', end='\t\t')

        print()
    print('_' * 90, '\n\n')

ispis_zaglavlja_tablice()

ispisi_tijelo_tablice("Kamion")