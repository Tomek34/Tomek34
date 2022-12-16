"""rijec = input("Unesi riječ za koju misliš da je palindrom: ")

lista_slova_1 = []
lista_slova_2 = []

for znak in rijec:
    lista_slova_1.append(znak)

lista_slova_2 = list(reversed(lista_slova_1))

if lista_slova_1 == lista_slova_2:
    print(f'Riječ "{rijec}" je palindrom')
else:
    print(f'Riječ "{rijec}" nije palindrom')


# Primjer slice-a:

obrnuta_rijec = rijec[::-1]

if obrnuta_rijec == rijec:
        print(f'Riječ "{rijec}" je palindrom')
else:
    print(f'Riječ "{rijec}" nije palindrom')



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

# HEADER TABLE ROW
print()
print('_' * 90)
header_top_line = 'ID\tTip\t\tProizvodac\t\tRegistarska\t\tGodina prve\t\tCijena'
header_bottom_line = '  \t   \t\t          \t\toznaka\t\t\tregistracija\t\t(EUR)'
print(header_top_line, '\n', header_bottom_line)
print('_' * 90, '\n')

for kljuc, vrijednost in vozni_park.items():
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


for kljuc, vrijednost in vozni_park.items():
    print(f'{kljuc}', end='\t')
    for element in vrijednost:
        prvi_uvjet = type(element) == str
        if prvi_uvjet:
            if len(element) > 9:
                print(f'{element}', end='\t')
            else:
                print(f'{element}', end='\t\t')
        else:
            print(f'{element}', end='\t\t')
    print()


# skraćeno
for kljuc, vrijednost in vozni_park.items():
    print(f'{kljuc}', end='\t')
    for element in vrijednost:
        prvi_uvjet = type(element) == str
        if prvi_uvjet and len(element) > 9:
             print(f'{element}', end='\t')
        else:
            print(f'{element}', end='\t\t')
    print()


# skraćeno
for kljuc, vrijednost in vozni_park.items():
    print(f'{kljuc}', end='\t')
    for element in vrijednost:
        if type(element) == str and len(element) > 9:
             print(f'{element}', end='\t')
        else:
            print(f'{element}', end='\t\t')
    print()"""