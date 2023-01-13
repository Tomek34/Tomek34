import json
from multiprocessing import Value

ime_datoteke = "vjezba_json_ban_jelacic.json"

print(f"{ime_datoteke} ima sadržaj: ")

with open(ime_datoteke, "r") as datoteka_koju_citamo:
    linije = datoteka_koju_citamo.readlines()
    for linija in linije:
        print(linija.rstrip())
        dict_linija = json.loads(linija)
        print(dict_linija['Jezici'])
        for key, value in dict_linija.items():
            print(f'Na ključu {key} je vrijednost {value}.')