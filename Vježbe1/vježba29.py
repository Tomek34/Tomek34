# napisati funkciju koja prima 2 broja i vraća rezultat množenja ta dva broja
# korištenjem te funkcije pomnožiti 23, 32 i 45
# ispisati rezultat
# korištenjem funkcije koju smo danas napisali za zbrajanje 2 broja
# zbrojiti taj umnožak sam sa sobom i ispisati rezultat

def funkcija_množenje(broj_1, broj_2):
    rezultat = broj_1 * broj_2
    return rezultat

prvi_umnozak = funkcija_množenje(23, 32)
drugi_umnozak = funkcija_množenje(prvi_umnozak, 45)
print(drugi_umnozak)

def funkcija_zbrajanje(drugi_umnozak):
    rezultat_2 = drugi_umnozak + drugi_umnozak
    return rezultat_2

zbroj = funkcija_zbrajanje(drugi_umnozak + drugi_umnozak)
print(zbroj)