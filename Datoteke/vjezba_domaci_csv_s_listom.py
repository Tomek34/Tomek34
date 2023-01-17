from importlib.resources import path
import os

from vjezba_domaci import provjeri_jel_file_postoji

def prvojeri_jel_file_postoji(ime_datoteke):
    """vraća True ako datoteka postoji, a ako ne vratiti False"""
    return os.path.exists(ime_datoteke)

# ZADATAK 2:
# korištenjem vjeba_pisanje_csv_u_file.py i rješenjem za čitanje iz CSV filea
# pokušati napuniti dict kako bi dobili iste podatke u dictu kakve imamo u vjeba_pisanje_csv_u_file.py
# tako da vrijednosti_za_upis bude jednak vrijednosti_za_ispis

ime_datoteke = "vjezba_csv_ban_jelacic.csv"

def procitaj_csv_iz_datoteke(ime_datoteke):
    dict_kojeg_citamo ={}
    with open(ime_datoteke, "r") as datoteka_koju_citamo:
        linije = datoteka_koju_citamo.readlines()
        for linija in linije:
            # linija je zarezom odvojen niz znakova
            # prvi string prije zareza je ključ, ostalo je vrijednost
            vrijednost_linije = linija.rstrip().split(',')
            if len(vrijednost_linije) == 2:
                kljuc = vrijednost_linije[0]
                dict_kojeg_citamo[kljuc] = vrijednost_linije[1]
            if len(vrijednost_linije) > 2:
                kljuc = vrijednost_linije[0]
                lista_jezika = []
                for jezik in vrijednost_linije[1:]:
                    # jezik.strio().strip("'[]") znači
                    # .strip() -> miče prvi razmak koji nam smeta
                    # -strip("'[]") -> miče ostale znakove koji nam smetaju
                    vrijednost_za_u_dict = jezik.strip().strip("'[]")
                    lista_jezika.append(vrijednost_za_u_dict)
                dict_kojeg_citamo[kljuc] = lista_jezika
            # problem sa jezicima: "['hrvatski'", "'njemački']"
    return dict_kojeg_citamo

if provjeri_jel_file_postoji(ime_datoteke):
    dobiveni_dict = procitaj_csv_iz_datoteke(ime_datoteke)
    for key, value in dobiveni_dict.items():
        print(f'{key}: {value}')
else:
    print(f"{ime_datoteke} ne postoji.")