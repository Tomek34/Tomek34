# WHILE petlja

# IF petlja je imala uvjet za koji, ako je ispunjen, izvršava se blok programskog koda te petlje SAMO JEDNOM.
# Nakon završetka bloka programskog koda IF petlje, program se nastavlja izvršavati dalje, izvan IF petlje.
# WHILE petlja je slična. Isto tako ima uvjet koji ako je ispunjen, osigurava pokretanje bloka programskog koda
# unutar WHILE petlje, ali nakon završetka tog bloka programskog koda, WHILE petlja će ponoviti provjeru uvjeta.
# Ako je uvjet ispunjen, OPET će se ponoviti isti blok programskog koda.
# While uvjet: 


"""brojevi = []

for broj in range(1, 21):
    brojevi.append(broj)

for broj in brojevi:
    print(broj, end=' ')

print()

brojac = 0

while brojac < len(brojevi):
    print(brojevi[brojac], end=' ')
    brojac += 1
print()


brojevi_za_while = []

brojac = 1

while brojac < 21:
    brojevi_za_while.append(brojac)
    brojac += 1

while brojac < len(brojevi_za_while):
    print(brojevi_za_while[brojac], end=' ')
    brojac += 1
print()"""



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

broj_elemenata_u_dictu = len(vozni_park)

key = 1
while key <= broj_elemenata_u_dictu:
    print(key, end='\n\t')
    brojac_elemenata = 0
    while brojac_elemenata < len(vozni_park[key]):
        print(vozni_park[key][brojac_elemenata], end='\n\t')
        brojac_elemenata += 1
    print()
    key += 1

for key in vozni_park.keys():
    print(key, end='\n\t')
    for element in vozni_park[key]:
            print(element, end=',\t')
    print()
print()