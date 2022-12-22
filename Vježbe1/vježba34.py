"""def maskiraj_sve_osim_zadnja_4(broj_kartice, maska):
    radna_kartica = broj_kartice.copy()
    counter = 1
    for i in reversed(range(len(radna_kartica))):
        if radna_kartica[i].isdigit() == True:
            if counter < 5:
                radna_kartica[i] = maska
                counter +=1
    return ''.join(radna_kartica)

def unesi_i_maskiraj_karticu():
    broj_kartice = list(input("Unsei broj kartice: "))
    maska = input("Odaberi znak kojim ćeš zaštititi broj kartice: ")
    print(maskiraj_sve_osim_zadnja_4(broj_kartice, maska))

unesi_i_maskiraj_karticu()"""

# Primjer broja kartice

"""def maskiraj_sve_osim_zadnja_4(broj_kartice, maska):
    # zaštitimo se da ne sakrivamo podatke koje ne možemo
    if len(broj_kartice) < 5:
        return 'Prekratak niz'

    radna_kartica = ''
    counter = 0
    zastita_pocinje = len(broj_kartice) - 4
    for znak in broj_kartice:
        if counter < zastita_pocinje:
            radna_kartica += maska
        else:
            radna_kartica += znak
        counter += 1
    return radna_kartica

def unesi_i_maskiraj_karticu():
    broj_kartice = (input("Unsei broj kartice: "))
    maska = input("Odaberi znak kojim ćeš zaštititi broj kartice: ")
    print(maskiraj_sve_osim_zadnja_4(broj_kartice, maska))

unesi_i_maskiraj_karticu()"""

# Primjer broja kartice korištenjem znaka '-' između brojeva kartice

def maskiraj_sve_osim_zadnja_4(broj_kartice, maska):
    # zaštitimo se da ne sakrivamo podatke koje ne možemo
    if len(broj_kartice) < 5:
        return 'Prekratak niz'

    radna_kartica = ''
    counter = 0
    zastita_pocinje = len(broj_kartice) - 4
    for znak in broj_kartice:
        if znak == '-':
            radna_kartica += znak
        elif counter < zastita_pocinje:
            radna_kartica += maska
        else:
            radna_kartica += znak
        counter += 1
    return radna_kartica

def unesi_i_maskiraj_karticu():
    broj_kartice = (input("Unsei broj kartice: "))
    maska = input("Odaberi znak kojim ćeš zaštititi broj kartice: ")
    print(maskiraj_sve_osim_zadnja_4(broj_kartice, maska))

unesi_i_maskiraj_karticu()