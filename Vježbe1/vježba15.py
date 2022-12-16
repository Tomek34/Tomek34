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

kljuc_tip = "tip"
kljuc_proizvodjac = "proizvođač"
kljuc_registracija = "registarska oznaka"
kljuc_godina_registracije = "prva godina registracije"
kljuc_cijena_u_eurima = "cijena u EUR"

# ZADATAK: vozni_park prepisati u novi dic
# Novi dict će imati elemente koji imaju isti ključ
# ali vrijednost će biti dic sa ključevima definiranim gore
# vozni_park_sa_dci_u_value = {1: {"tip": "", "proizvođač": "", "registarska oznaka": "",
# "prva godina registracije": "", "cijena u EUR"_: ""}}

# HINT:

vozni_park_sa_dict_u_value = {}

for kljuc, vrijednost in vozni_park.items():
    vrijednost_dict = {
        kljuc_tip: vrijednost[0],
        kljuc_proizvodjac: vrijednost[1],
        kljuc_registracija: vrijednost[2],
        kljuc_godina_registracije: vrijednost[3],
        kljuc_cijena_u_eurima: vrijednost[4]
    }
    vozni_park_sa_dict_u_value[kljuc] = vrijednost_dict

for k, v in vozni_park_sa_dict_u_value.items():
    print(f'k={k}, v={v}')
print()

vozni_park_sa_dict_u_value.clear()

for kljuc, vrijednost in vozni_park.items():
    vozni_park_sa_dict_u_value[kljuc] = {
        "tip": vrijednost[0],
        "proizvođač": vrijednost[1],
        "registarska oznaka": vrijednost[2],
        "prva godina registracije": vrijednost[3],
        "Cijena u EUR": vrijednost[4]
    }

for k, v in vozni_park_sa_dict_u_value.items():
    print(f'{k} = ')
    for vrijednost_kljuc, vrijednost in v.items():
        print(f'{vrijednost_kljuc} = {vrijednost}')
    print()
print()


# ZADATAK: iz vozni_park_sa_dict_u_value ispisati registarsku oznaku i godinu prve registracije za elemente ključem 1, 3, 5 i 7

print(vozni_park_sa_dict_u_value[1]["registarska oznaka"],vozni_park_sa_dict_u_value[1]["prva godina registracije"])"""