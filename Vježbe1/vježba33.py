# CREDIT CARD MASK

"""str = "CREDITCARDNUMBER"
strlenght = len(str)
masked = strlenght - 4
slimstr = str[masked:]
print('*'*masked+slimstr)"""

"""str = "CREDITCARDNUMBER"
strlenght = len(str)
sto_zelimo_sakriti = strlenght - 4
sve_sto_treba_biti_citljivo = str[sto_zelimo_sakriti:]
print('*'*sto_zelimo_sakriti + sve_sto_treba_biti_citljivo)"""

# PONAVLJANJE LISTE

"""lista_1 = [1, 2, 3, 4, 5]
# ispis broj elemenata u listi
print(len(lista_1))
# ispis prvog elementa u listi
print(lista_1[0])
# ispis zadnjeg elementa u listi
print(lista_1[-1])
print(lista_1[3])
# ispis srednjeg elementa u listi
print(lista_1[2])
print(lista_1[-3])
# 'školski' primjer ispisa elementa u listi
print(lista_1[len(lista_1)//2])
print((len(lista_1)-1))
# ispis više elemenata na indexu unutar liste
print(lista_1[1], lista_1[2])
# ispis nove liste elemenata unutar postojeće liste
print(lista_1[1:3])
print(lista_1[1:3:2])


lista_1 = [1, 2, 3, 4]

i = 1
kraj = 3
korak = 2

print(lista_1[i:kraj:korak])

for element in lista_1:
    if lista_1.index(element) == i:
        print(lista_1[i])
        i += korak
    if i == kraj:
        break"""

"""lista_voce = ["banana"]
#print(lista_voce)
print(lista_voce.append("jabuka"))
#print(lista_voce)

# dodavanje novog elementa u listu
lista_voce.insert(1, "kruška")
print(lista_voce)

# zamjena postojećeg elementa u listi
lista_voce[1] = "kruška"
print(lista_voce)"""

# VJEŽBA BROJ KARTICE

"""broj_kartice = "NEKSTRING"

lista_slova = []
for slovo in broj_kartice:
    lista_slova.append(slovo)

print(lista_slova)

print(lista_slova[0:len(lista_slova)-4-1])
print(broj_kartice[0:len(broj_kartice)-4-1])"""

"""print(broj_kartice[0:len(broj_kartice)-4])

maskirani_broj_kartice = ""
prvi_nemaskirani_index = len(broj_kartice) - 4
index_u_stringu = 0

for slovo in broj_kartice:
    if index_u_stringu < prvi_nemaskirani_index:
        maskirani_broj_kartice += "*"
    else:
        maskirani_broj_kartice += slovo
    index_u_stringu += 1

print(maskirani_broj_kartice)"""

# Zamijeniti znakove u broju kartice sa * osim ako su:
# znak '-' bez obzir gdje se nalazi u stringu
# zadnja četiri znaka

# primjer:
# broj_kartice = "NEKI-STRING-PERO"
# rezultat = "****-******-PERO"

"""broj_kartice = "NEKI-STRING-PERO"

print(broj_kartice[0:len(broj_kartice)-4])

maskirani_broj_kartice = ""
prvi_nemaskirani_index = len(broj_kartice) - 4
index_u_stringu = 0

for slovo in broj_kartice:
    if slovo =='-':
        maskirani_broj_kartice += slovo
    elif index_u_stringu < prvi_nemaskirani_index:
        maskirani_broj_kartice += '*'
    else:
        maskirani_broj_kartice += slovo
    index_u_stringu += 1

print(maskirani_broj_kartice)"""

"""# VJEŽBA PETLJE

# primjer 'for' petljom:
niz = [1,2,3,4,5]
# početak 'for' petlje
for element in niz:
    print(element)
# kraj 'for' petlje
print('Gotova for petlja.')

# primjer 'while' petljom:
# početak 'while' petlje
koliko_puta_cemo_se_zavrtiti = len(niz)

broj_vrtnji = 0

while broj_vrtnji < koliko_puta_cemo_se_zavrtiti:
    print(niz[broj_vrtnji])
    broj_vrtnji += 1
    # Dokle god je zadovoljen uvjet u 'while' petlji, ona neće prestati s radom.
# kraj 'while' petlje
print('Gotova while petlja.')"""

"""soptina_lista = ['banana', 'mango', 'kiwi']
# ispisati samo 'kiwi' korištenjem slice naredbe
soptina_lista.append("jagoda")

print(soptina_lista[2])
print(soptina_lista[-1])
print(soptina_lista[2:3][0])
# vraća listu koja nije soptina_lista nego nova lista"""

# VJEŽBA WHILE PETLJA

# dok ima francuske, jedi svinjetinu

"""francuska = 100 # puna zdjela francuske
jedna_zlica = 5 # praznimo zdjelu

while francuska > 0:
    print(f'Ostalo nam je {francuska/jedna_zlica} za pojesti.')
    francuska -= jedna_zlica"""

# VJEŽBA FOR PETLJA

# Vlak ima lokomotivu i sve vagone

vlak = []
vagoni = ['vagon 1', 'vagon 2', 'vagon 3', 'vagon 4', 'vagon 5']

for vagon in vagoni:
    vlak.append("lokomotiva")
    vlak.extend(vagoni)
    break
print(vlak)

"""vlak = []
vagoni = ['vagon 1', 'vagon 2', 'vagon 3', 'vagon 4', 'vagon 5']

vlak.append("lokomotiva") # lista vlak ima 1 element i to je lokomotiva

for vagon in vagoni:
    vlak.append(vagon)

print(vlak)"""