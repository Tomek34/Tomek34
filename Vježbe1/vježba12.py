#ZADATAK: Napišite program koji kreira akorde na osnovu početnog tona, odnosno note.
    #POJAŠNJENJE
    #Akord se sastoji od tri tona koji se mogu ponavjljati.
    #Durski akord čine: početni ton, 4. ton te 7. ton.
        #Označava se samo velikim slovom početnog tona ili velikim slovom početnog tona uz dodatak dur.
    #Molski akord čine: početni ton, 3. ton te 7. ton.
        #Označava se samo malim slovom početnog tona ili malim slovom početnog tona uz dodatak mol.

    #Glazbena abeceda: C, C#, D, D#, E, F, F#, G, G#, A, A#, H
    #Engleska oznaka za H ton je B pa oni imaju A B C D E F G pa novi kruog od A B


import sys


tonovi_dur = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
tonovi = tonovi_dur
tonovi_mol = []
for ton in tonovi:
    tonovi_mol.append(ton.lower())
print(tonovi_mol)

drugi_index_durski = 4
treci_index_durski = 7

odabrani_ton = input("Unesi ton od kojeg želiš napraviti akord: ")

if odabrani_ton in tonovi_mol:
    drugi_index_durski = 3
    tonovi = tonovi_mol

elif odabrani_ton not in tonovi_dur:
    print(f'Pero, ti si mi malo nestašan? {odabrani_ton} nije nota!')
    sys.exit(1)

duljina_liste_tonova = len(tonovi_dur)
print(f'duljina liste tonova je: {duljina_liste_tonova}')
print(f'prvi ton akorda je: {odabrani_ton}')
index_odabranog_tona = tonovi.index(odabrani_ton)
print(f'njegov index je: {index_odabranog_tona}')

print(f'sljedeća pozicija u listi je: {(index_odabranog_tona+drugi_index_durski)%duljina_liste_tonova}')
print(f'sljedeća pozicija u listi bez modula bi bila: {(index_odabranog_tona+drugi_index_durski)}')
drugi_ton_akorda = tonovi_dur[(index_odabranog_tona+drugi_index_durski)%duljina_liste_tonova]
print(f'drugi ton akorda je: {drugi_ton_akorda}')

print(f'treća pozicija u listi je: {(index_odabranog_tona+treci_index_durski)%duljina_liste_tonova}')
print(f'zadnja pozicija u listi bez modula bi bila: {(index_odabranog_tona+treci_index_durski)}')
treci_ton_akorda = tonovi_dur[(index_odabranog_tona+treci_index_durski)%duljina_liste_tonova]
print(f'treći ton akorda je: {treci_ton_akorda}')