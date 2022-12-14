"""vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'TAM', 'ST 001 ZZ', 2013, 97000.00],
    6 : ['Kombi', 'FAP', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'FAP', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'FAP', 'ZG 002 ZZ', 2010, 9300.00]
}

vozni_park_sa_dict_u_value = {}


for kljuc, vrijednost in vozni_park.items():
    vozni_park_sa_dict_u_value[kljuc] = {
        "tip": vrijednost[0],
        "proizvođač": vrijednost[1],
        "registarska oznaka": vrijednost[2],
        "prva godina registracije": vrijednost[3],
        "Cijena u EUR": vrijednost[4]
    }

# Dodavanje novog Kljuca u Rječnik:

vozni_park[9] = ['Dostavno vozilo', 'FAP', 'ZG 002 ZZ', 2010, 9300.00]

print(vozni_park.keys())
print(vozni_park[9])

# Provjera zadnjeg Kljuca u Rječniku:

zadnji_kljuc_ako_znamo_da_su_svi_int = sorted(vozni_park.keys(), reverse=True)[0]
print(zadnji_kljuc_ako_znamo_da_su_svi_int)
print(vozni_park[zadnji_kljuc_ako_znamo_da_su_svi_int])"""