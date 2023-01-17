import os
import json

import requests

def provjeri_jel_file_postoji(ime_datoteke):
    """vraća True ako datoteka postoji, a ako ne vrati False"""
    return os.path.exists(ime_datoteke)

def procitaj_json_iz_datoteke(ime_datoteke):
    with open(ime_datoteke, "r", encoding="utf-8") as datoteka_koju_citamo:
        procitani_dict = json.load(datoteka_koju_citamo)
        print(procitani_dict)

def upisi_json_u_datoteku(ime_datoteke, vrijednosti_za_upis):
    with open(ime_datoteke, "w", encoding="utf-8") as datoteka_u_koju_pisemo:
        json.dump(vrijednosti_za_upis, datoteka_u_koju_pisemo, indent=4)

def dohvati_podatke_s_urla(url):
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        # dobili smo listu dictova
        json_s_weba = response.json()
    else:
        json_s_weba = []
    return json_s_weba

def ispisi_dict(dict_s_weba):
    print(json.dumps(dict_s_weba, indent=4))

URL = "https://jsonplaceholder.typicode.com/posts"

lista_dictova = dohvati_podatke_s_urla(URL)

# ZADATAK: ispisati podatke za dict koje je na indeksu 2 u lista_dictova
# koristiti ispisi_dict

ispisi_dict(lista_dictova[2])


# ZADATAK:
# 1. dohvatiti listu postova sa URL-a, ako nije u lista_dictova
# 2. ako ne postoji datoteka naziva "post_s_weba.json":
#   	dict koji je na indesku 2 u lista_dictova zapisati u datoteku
# 3. ako datoteka postoji:
#   pročitati što piše u njoj, a dict s weba samo ispisati

def provjeri_jel_file_postoji(post_s_weba):
    return os.path.exists(post_s_weba)