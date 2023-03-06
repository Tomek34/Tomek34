import requests
from zajednicko.rezultat_mjerenja import RezultatMjerenja

base_url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,surface_pressure&current_weather=true&timezone=auto"

def dohvati_prognozu(url, latitude, longitude):
    return requests.get(url.format(latitude=latitude, longitude=longitude)).json()

def obradi_prognozu(podaci):
    data = {}
    hourly_data = podaci.get("hourly", {})
    for indeks, vrijeme in enumerate(hourly_data.get("time", [])):
        # ZADATAK: tu koristiti klasu, a ne dict. 
        # Klasa mora biti ista kao i u simulator senzora SensorZaRaspberryPi.dohvati_podatke
        # napomena: tu će biti 3 objekta, ne 1
        data[vrijeme] = {
            "TEMPERATURA": hourly_data["temperature_2m"][indeks],
            "TLAK": hourly_data["surface_pressure"][indeks],
            "VLAGA": hourly_data["relativehumidity_2m"][indeks],
        }
    return data


def obradi_prognozu_s_klasama(podaci):
    data = {}
    hourly_data = podaci.get("hourly", {})
    for indeks, vrijeme in enumerate(hourly_data.get("time", [])):
        # ZADATAK: tu koristiti klasu, a ne dict. 
        # Klasa mora biti ista kao i u simulator senzora SensorZaRaspberryPi.dohvati_podatke
        # napomena: tu će biti 3 objekta, ne 1
        data[vrijeme] = [
            RezultatMjerenja(vrijednost=hourly_data["temperature_2m"][indeks], mjerna_jedinica="°C", tip="TEMPERATURA"),
            RezultatMjerenja(vrijednost=hourly_data["surface_pressure"][indeks], mjerna_jedinica="hPa", tip="TLAK"),
            RezultatMjerenja(vrijednost=hourly_data["relativehumidity_2m"][indeks], mjerna_jedinica="%", tip="VLAGA"),
        ]
    return data
