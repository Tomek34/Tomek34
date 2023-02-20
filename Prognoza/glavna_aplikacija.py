import os
import json
from prognoza_vremena import WeatherForecast
from senzor_app import Sensor

def print_data(temperature, humidity, pressure):
    print(f"Temperatura je {temperature} °C.")
    print(f"Vlažnost zraka je {humidity} %.")
    print(f"Tlak zraka je {pressure} hPa.")

def save_data(temperature, humidity, pressure):
    data = {
        'temperatura': temperature,
        'vlažnost zraka': humidity,
        'tlak zraka': pressure, 
    }
    file_path = os.path.join('ispis', 'data.json')
    with open (file_path, 'w') as f:
        json.dump (data, f, indent=4)
    print(f"Data saved to {file_path}")

def main():
    city = 'Krapina'
    weather_forecast = WeatherForecast(city)
    data = weather_forecast.get_forecast()

    if data is not None:
        temperature, humidity, pressure = data
        print("Prognoza vremena za {city}:")
        print_data(temperature, humidity, pressure)

    if temperature > 23:
        print("Temperatura je veća od 23°C.")
    else:
        print("Temperatura je manja od 23°C.")
    if humidity < 75:
        print("Vlažnost zraka je manja od 50%.")
    else:
        print("Vlažnost zraka je veća od 50%.")
    if pressure < 1012:
        print("Tlak zraka je manji od 1012 hPa.")
    else:
        print("Tlak zraka je veći od 1012 hPa.")

sensor = Sensor
sensor.read_data()
print("Sensor data: ")
print_data(sensor.temperature, sensor.humidity, sensor.pressure)
save_data(sensor.temperature, sensor.humidity, sensor.pressure)