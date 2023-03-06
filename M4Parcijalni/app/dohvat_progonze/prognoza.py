import requests

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

class WeatherData:
    def __init__(self, temperature, pressure, humidity):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity

def get_weather_forecast(url, latitude, longitude):
    response = requests.get(url.format(latitude=latitude, longitude=longitude)).json()
    data = {}
    hourly_data = response.get("hourly", {})
    for index, time in enumerate(hourly_data.get("time", [])):
        data[time] = [
            WeatherData(
                hourly_data["temperature_2m"][index],
                hourly_data["surface_pressure"][index],
                hourly_data["relativehumidity_2m"][index],
            )
        ] * 3
    return data