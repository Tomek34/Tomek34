# ZADATAK 1:
# pokušati umjesto json.loads koristiti jason.load -> pogledati dokumentaciju za json modul u Pythonu.


import json

def procitaj_json_iz_datoteke(ime_datoteke):
    with open(ime_datoteke, "r", encoding="utf-8") as datoteka_koju_citamo:
        procitani_dict = json.load(datoteka_koju_citamo)

ime_datoteke = "vjezba_json_ban_jelacic.json"

procitaj_json_iz_datoteke(ime_datoteke)


# ZADATAK 2:
# korištenjem vjeba_pisanje_csv_u_file.py i rješenjem za čitanje iz CSV filea
# pokušati napuniti dict kako bi dobili iste podatke u dictu kakve imamo u vjeba_pisanje_csv_u_file.py
# tako da vrijednosti_za_upis bude jednak vrijednosti_za_ispis