import requests
import json

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

"""for mozda_dict in lista_dictova[0:1]:
    for key in mozda_dict.items():
        print(f'{key}')"""

ispisi_dict(lista_dictova[2])