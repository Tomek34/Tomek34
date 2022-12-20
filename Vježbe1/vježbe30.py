# FUNKCIJA PALINDROM

"""def provjera_palindrom(rijec):
    lista_slova_2 = rijec[::-1]

    if rijec == lista_slova_2:
        return True
    else:
        return False

rijec = input("Unesi riječ za koju misliš da je palindrom: ")
rijec = rijec.lower()

rezultat = provjera_palindrom(rijec)

if rezultat:
    print(f'Rijec {rijec} je palindrom.')
else:
    print(f'Rijec {rijec} nije palindrom.')

# SKRAĆENI NAČIN FUNKCIJE

def provjera_palindrom(rijec):
    return rijec == rijec[::-1]

rijec = input("Unesi riječ za koju misliš da je palindrom: ").lower()

rezultat = provjera_palindrom(rijec)

if rezultat:
    print(f'Rijec {rijec} je palindrom.')
else:
    print(f'Rijec {rijec} nije palindrom.')"""



# GLOBALNE VARIJABLE    

"""PI = 3.141512

def opseg_kruga(radijus):
    return 2*radijus*PI

radijus = 12
print(opseg_kruga(10))
print(radijus)
print(opseg_kruga(radijus))"""

PI = 3.141512

def opseg_kruga(radijus):
    return 2*radijus*PI

def površina_kruga(radijus):
    return radijus*radijus*PI

print(opseg_kruga(10))
print(površina_kruga)



# FUNKCIJE I ARGUMENTI

"""def ispisi(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)

ispisi("Ante", "Stipe", sep="\tPERO\t", end="\t")

def ispisi(*args, separator=' ', kraj_niza='\n'):
    print(*args, sep=separator, end=kraj_niza)

ispisi("Ante", "Stipe")"""