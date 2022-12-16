""""""#Kreirajte bazu s vozilima firme. ID svakog retka je cijeli broj, a podaci koji se čuvaju o svakom vozilu su:
#tip, proizvođač, registarska oznaka, godina prve registracije te cijena u eurima. Ispišite cijelu tablicu tako da ID
#odvojite od ostatka retka jednim TABom, a druge informacije formatirajte tako da prvi red tablice predstavlja naslovni red,
#a ostali redovi tablice predstavljaju podatke iz baze.


"""vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 97000.00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00]
}


# HEADER TABLE ROW
header_top_line = 'ID\tTip\t\tProizvodac\t\tRegistarska\t\tGodina prve\t\tCijena'
header_bottom_line = '  \t   \t\t          \t\toznaka\t\t\tregistracija\t\t(EUR)'
header_under_line = '_' * 105
print(header_top_line, '\n', header_bottom_line, '\n', header_under_line)


# BODY TABLE ROWs
#for kljuc in vrijednost.items() ako tražimo listu Ključeva i Vrijednosti unutar tablice.
for kljuc in vozni_park.keys():
    vrijednost = vozni_park[kljuc]
    print(f'{kljuc}', end='\t')
    for element in vrijednost:
        print(f'{element}', end='\t\t')
    print()


vozni_park.clear()
for kljuc in vozni_park.keys():
    vrijednost = vozni_park[kljuc]
    print(f'{kljuc}', end='\t')
    for element in vrijednost:
        print(f'{element}', end='\t')
    print()


fap = vozni_park.pop(6)
print(f'maknuta vrijednost = {fap}')

print('vozni park nakon micanja')
for kljuc in vozni_park.keys():
    vrijednost = vozni_park[kljuc]
    print(f'{kljuc}', end='\t')
    for element in vrijednost:
        print(f'{element}', end='\t\t')
    print()

fap = vozni_park.pop(6, "nemamo 6 u voznom parku")
print(fap)

zadnji_fap = vozni_park.popitem()
print(zadnji_fap)

#popitem je zadnji ključ u rječniku, briše i vraća nazad i ključ i vrijednost

print('vozni park nakon pop(6)')
for kljuc in vozni_park.keys():
    vrijednost = vozni_park[kljuc]
    print(f'{kljuc}', end='\t')
    for element in vrijednost:
        print(f'{element}', end='\t\t')
    print()

nova_vrijednost_za_5 = ['Kombi', 'PERO', 'ST 001 ZZ', 2021, 1200000.00]
vozni_park[5] = nova_vrijednost_za_5
print(f'kljuc=5, vrijednost{vozni_park}')


for kljuc in vozni_park:
    vrijednost = vozni_park[kljuc]
    print(f'kljuc={kljuc}, vrijednost{vrijednost}')
print()

print(len(vozni_park))
print(vozni_park[len(vozni_park)])

vozni_park['a'] = ["ovo je zadnje dodan vrijednost u vozni park"]
print(vozni_park.popitem())
for kljuc in vozni_park.keys():
    vrijednost = vozni_park[kljuc]
    print(f'{kljuc}', end='\t')
    for element in vrijednost:
        print(f'{element}', end='\t\t')
    print()"""

# ZADATAK: u vozni_park ključu 1 promijeniti vrijednost na indexu 1 iz 'Iveco' u 'STIPE'
# koristiti 1 naredbu
# ispisati vrijednost

"""print(vozni_park[1][1])
vozni_park[1][1] = "STIPE"

for element in vozni_park[1]:
    print(element, end= " ")

print(vozni_park[1][1])
for k in vozni_park:
    print(f'k={k}, v={vozni_park[k]}')


# ZADATAK:u vozni_park ključu 1 dodati vrijednost "100" n kraj liste
# koristiti naredbu za dodavanje elemenata na kraj liste
# ispisati vrijednost od indeksa 3 do kraja


vozni_park[1].append("100")
print(vozni_park[1][3:])
print(vozni_park[1])

# ZADAKAT: iz vozni_park maknuti element koji ima ključ 6
# vrijednost tog elementa prdjeliti umjesto trenutne vrijednosti
# elementu koji ima ključ 8

print(vozni_park[6])
print(vozni_park[8])
# maknuta_vrijednost_sa_6 = vozni_park.pop(6)
# vozbi_park[8] = maknuta_vrijednost_sa_6
vozni_park[8] = vozni_park.pop(6)
print(vozni_park[8])


# ZADATAK: iz vozni_park maknuti element koji ima ključ 19,
# ako u vozni_park ne postoji element koji ima ključ 19,
# vrijednost neka bude 'Element sa ključem 19 ne postoji!'
# ispiši dobivenu vrijednost

maknuta_vrijednost_sa_19 = vozni_park.pop(19, 'Element sa ključem 19 ne postoji!')
print(maknuta_vrijednost_sa_19)

# ZADATAK: u vozni park dodati element sa ključem 19
# i vrijednošću ['avion', 'MIG', 'F-19', 2022, 0.001]
# ponoviti prethodni zadatak
# koja je sad dobivena vrijednost iz prethodnog zadatka?

vozni_park[19]=['avion', 'MIG', 'F-19', 2022, 0.001]

maknuta_vrijednost_sa_19_opet = vozni_park.pop(19, 'Element sa ključem 19 ne postoji!')
print(maknuta_vrijednost_sa_19_opet)
#print(f'Ovo bi trebalo biti False. Da li je: {maknuta_vrijednost_sa_19_opet == maknuta_vrijednost_sa_19}')

print(vozni_park.get(19, "Nema ga!!!!"))
print(vozni_park.get(19))

print(vozni_park[19])

# Get ne briše element
# Ako nema elementa s tim ključem, vraća grešku

print(vozni_park.get(19, "Ključa 19 nema"))

try:
    print(vozni_park[19])
except KeyError:
    print('Ključa 19 nema')

for kljuc, vrijednost in vozni_park.items():
    print(f'{kljuc}', end='\t')
    for element in vrijednost:
        print(f'{element}', end='\t')
    print()"""