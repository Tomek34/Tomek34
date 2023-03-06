import json
import pathlib

from dohvat_progonze.prognoza import dohvati_prognozu, base_url, obradi_prognozu, obradi_prognozu_s_klasama
from senzori.simulator_senzora import raspberry_pi
import ispis


def load_configuration():
    putanja_do_ovog_filea = pathlib.Path(__file__).parent
    configuration_file = putanja_do_ovog_filea.joinpath("config.json")
    if configuration_file.exists():
        with open(configuration_file.absolute(), "r", encoding="utf-8") as konfiguracijski_file:
            konfiguracija = json.load(konfiguracijski_file)
    else:
        print("Ne postoji konfiguracija")
        konfiguracija = {"latitude": 45.14, "longitude": 14.66}
    return konfiguracija

def dohvati_podatke_i_usporedi_ih(konfiguracija):
    podaci = dohvati_prognozu(base_url, konfiguracija["latitude"], konfiguracija["longitude"])
    ispis.ispisi_json(podaci)
    prognoza = obradi_prognozu(podaci)
    for vrijeme, podaci_u_to_vrijeme in prognoza.items():
        podaci_senzora = raspberry_pi.get_data()
         
        for sensor_data in podaci_senzora:
            # ZADATAK: tu korisiti usporedbu vrijednosti atributa dvije klase
            # podaci_u_to_vrijeme.vrijednost == sensor_data.vrijednost
            # igranje s dictom!
            if podaci_u_to_vrijeme[sensor_data["ime"]] != sensor_data["vrijednost"]:
                print(f'Podaci s weba u {vrijeme} za {sensor_data["ime"]} su različiti od podataka sa senzora : {podaci_u_to_vrijeme[sensor_data["ime"]]}{sensor_data["mjerna_jedinica"]} != {sensor_data["vrijednost"]}{sensor_data["mjerna_jedinica"]}')
            else:
                print(f'Podaci s weba u {vrijeme} za {sensor_data["ime"]} su isti kao i podatci sa senzora : {podaci_u_to_vrijeme[sensor_data["ime"]]}{sensor_data["mjerna_jedinica"]} == {sensor_data["vrijednost"]}{sensor_data["mjerna_jedinica"]}')


def dohvati_podatke_i_usporedi_ih_klase(konfiguracija):
    podaci = dohvati_prognozu(base_url, konfiguracija["latitude"], konfiguracija["longitude"])
    prognoza = obradi_prognozu_s_klasama(podaci)
    for vrijeme, podaci_u_to_vrijeme in prognoza.items():
        podaci_senzora_klasa = raspberry_pi.get_data_with_class()
        for sensor_data in podaci_senzora_klasa:
            for podaci_iz_prognoze in podaci_u_to_vrijeme:
                if sensor_data.tip == podaci_iz_prognoze.tip:
                    if podaci_iz_prognoze.vrijednost != sensor_data.vrijednost:
                        print(f'Podaci s weba u {vrijeme} za {sensor_data.tip} su različiti od podataka sa senzora : {podaci_iz_prognoze.vrijednost}{podaci_iz_prognoze.mjerna_jedinica} != {sensor_data.vrijednost}{sensor_data.mjerna_jedinica}')

if __name__ == "__main__":
    konfiguracija = load_configuration()
    dohvati_podatke_i_usporedi_ih_klase(konfiguracija)