#Dictionary ili Rječnik je kolekcija parova podataka-
#Rječnik koristi {} zagrade
#Svaki element Rječnika ima dva dijela:
    #Key ili Ključ
    #Value ili Vrijednost

#Key ili Ključ mora biti jedinstven u Rječniku. Zato jer Ključ mora biti jedinstven.
#Dopušteni tipovi podataka za Ključ su:
    #String, brojevi, n-terac

#Pomoću Ključa pristupamo drugom dijelu para, odnosno podacima-
#Ključ je isto kao i Indeks u listi.

#Value ili Vrijednost predstavlja sadržaj koji želimo pohraniti u kolekciju.

#Manipulacija podacima unutar Rječnika:
    #naziv_rjecnika[key]
    #naziv_rjecnika.items()
    #naziv_rjecnika.keys()
    #naziv_rjecnika.values()
    #naziv_rjecnika.clear()
    #naziv_rjecnika.pop(key, default)
    #naziv_rjecnika.popitem()


"""dictionary = {
    "voce": ["banana", "jabuka"],
    "povrce": ["kupus", "mrkva"],
    1: "pero",
    (1, 2): 101
}

print(dictionary)
print(dictionary["voce"])
print(dictionary["povrce"])
print(dictionary[1])
print(dictionary[1, 2])

voce = dictionary["voce"]
print(voce[0])
print(dictionary.items())

for key, value in dictionary.items():
    print(f'ključ \"{key}" sadrži vrijednost {value}')

print(dictionary.keys())

kljuc_pero = (1)
kljuc_voce = "voce"
kljuc_povrce = "povrce"
lista_voce = ["banana", "jabuka"]
lista_povrce = ["kupus", "mrkva"]

rjecnik = {
    kljuc_voce: lista_voce,
    kljuc_povrce: lista_povrce,
    kljuc_pero: 101,
    1: "pero",
}
print(rjecnik)
print(rjecnik[kljuc_pero])

for vrijednost in rjecnik.values():
    print(f'rječnik ima vrijednost: {vrijednost}')

for ključ in rjecnik.keys():
    print(f'rječnik ima ključ: {ključ}')

rjecnik_2 = {}
for kljuc, vrijednost in [("pero", "ante"), (1, 101), ("pero", "stipe")]:
    print(f'kljuc= {kljuc}, vrijednost= {vrijednost}')
    rjecnik_2[kljuc] = vrijednost

print(rjecnik_2)


primjer_micanja_duplikata = {}
for k in [1,3,4,1,5]:
    print(k, end=', ')
    primjer_micanja_duplikata[k] = f"k{k}=Pero"
print()

for key, value in primjer_micanja_duplikata.items():
    print(f'key={key}, value={value}')


primjer_micanja_duplikata = {}
lista_vrijednosti = [1,3,4,1,5]
i = 0
for k in lista_vrijednosti:
    value = f"k{k}=Pero{i}"
    print(f'key={k}, value={value}')
    primjer_micanja_duplikata[k] = value
    i +=1
print()

for key, value in primjer_micanja_duplikata.items():
    print(f'key={key}, value={value}')"""