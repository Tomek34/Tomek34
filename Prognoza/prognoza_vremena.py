import requests

class WeatherForecast:
    def __init__(self, city):
        self.city = city
        self.api_url = f'https://api.open-meteo.com/v1/forecast?latitude=46.16&longitude=15.88&hourly=temperature_2m,relativehumidity_2m,pressure_msl={city}'

    def get_forecast(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json
            temperature = data['hourly']['temperature_2m'][0]['value']
            humidity = data['hourly']['humidity_2m'][0]['value']
            pressure = data['hourly']['pressure_msl'][0]['value']
            return temperature, humidity, pressure
        else:
            return None