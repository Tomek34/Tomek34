konverzija_km_u_milju = 0.06214

jedinica = input("Odaberi jedinicu 'km' za kilometre u milje , 'm' za milje u kilometre: ")

def konverzija(jedinica):
    if jedinica == "km":
        duljina = int(input("Unesi broj kilometara: "))
        return print(f'{duljina} kilometara je {duljina*konverzija_km_u_milju:.4f} milja.')

    elif jedinica == "m":
        duljina = int(input("Unesi broj milja: "))
        return print(f'{duljina} milja je {duljina/konverzija_km_u_milju:.4f} kilometara.')

    else:
        print("Ne znam pretvoriti ovo.")
        duljina = 0

konverzija(jedinica)

# DVIJE FUNKCIJE(DEFINICIJE)

def unesi_duljinu(duljina):
    if jedinica == "km":
        duljina = int(input("Unesi broj kilometara: "))
    elif jedinica == "m":
        duljina = int(input("Unesi broj milja: "))
    else:
        print("Ne znam pretvoriti ovo.")
        duljina = 0
    return duljina

def konverzija(jedinica, duljina):
    if jedinica == "km":
        print(f'{duljina} kilometara je {duljina*konverzija_km_u_milju:.4f} milja.')
    elif jedinica == "m":
        print(f'{duljina} milja je {duljina/konverzija_km_u_milju:.4f} kilometara.')
    else:
        print("Ne znam pretvoriti ovo.")
        duljina = 0

jedinica = input("Odaberi jedinicu 'km' za kilometre u milje , 'm' za milje u kilometre: ")
duljina = unesi_duljinu(jedinica)
konverzija(jedinica, duljina)


# PROVJERA UNOSA

def provjeri_unos(korisnicki_unos):
    if korisnicki_unos == 'km':
        return 'km'
    elif korisnicki_unos == 'm':
        return 'm'
    else:
        print("Ne znam pretvoriti ovo.")
        return -1

def unesi_duljinu(duljina):
    if jedinica == "km":
        duljina = int(input("Unesi broj kilometara: "))
    elif jedinica == "m":
        duljina = int(input("Unesi broj milja: "))
    else:
        print("Ne znam pretvoriti ovo.")
        duljina = 0
    return duljina

def konverzija(jedinica, duljina):
    if jedinica == "km":
        print(f'{duljina} kilometara je {duljina*konverzija_km_u_milju:.4f} milja.')
    elif jedinica == "m":
        print(f'{duljina} milja je {duljina/konverzija_km_u_milju:.4f} kilometara.')
    else:
        print("Ne znam pretvoriti ovo.")

while True:
    unos = input("Odaberi jedinicu 'km' za kilometre u milje , 'm' za milje u kilometre: ")
    jedinica = provjeri_unos(unos)
    if jedinica == -1:
        continue
    duljina = unesi_duljinu(jedinica)
    konverzija(jedinica,duljina)
    break