
from random import randint


class Jagodica:
    def __init__(self, senzori):
        self.senzori = senzori
    
    def get_data(self):
        data = []
        for senzor in self.senzori:
            data.append(senzor.dohvati_podatke())
        return data

class Sensor:
    name = "PERO"
    value = 0

    def dohvati_podatke(self):
        return f"{self.name} = {self.value}"

class TemperaturSensore(Sensor):

    def __init__(self):
        self.name = "TEMPERATURA"
        self.value = 0

    def generate_value(self):
        self.value = randint(-10, 100)

class TSensor(Sensor):
    name = "TEMPERATURA"

    def get_temperatura(self):
        self.value = 100

class HSensor(Sensor):
    name = "HUMIDITY"

    def get_vlaznost(self):
        self.value = 25

senzor_1 = Sensor()
senzor_temp = TemperaturSensore()

print(senzor_temp.dohvati_podatke())
    
for i in range(3):
    senzor_temp.generate_value()
    print(senzor_temp.dohvati_podatke())

senzor_2 = TSensor()
senzor_2.get_temperatura()
print(TSensor.name)

senzor_3 = HSensor()
senzor_3.get_vlaznost()

lista_senzora= [senzor_1, senzor_2, senzor_3]


jagodu = Jagodica(lista_senzora)
print(jagodu.get_data())


class SensorPrazan:
    def __init__(self, ime_senzora):
        self.name = ime_senzora
        self.value = 0

    def dohvati_podatke(self):
        self.value = 1012
        return f"{self.name} = {self.value}"


novi_senzori = []
novi_senzor_1 = SensorPrazan(ime_senzora="PERO")
novi_senzor_2 = SensorPrazan(ime_senzora="TEMPERATURA")
novi_senzor_3 = SensorPrazan(ime_senzora="HUMIDITY")
novi_senzori = [novi_senzor_1, novi_senzor_2, novi_senzor_3]
malina = Jagodica(novi_senzori)

print(malina.get_data())
print()


class SensorZaRaspberryPi:
    def __init__(self, ime_senzora, max_vrijednost, min_vrijednost, mjerna_jednica):
        self.name = ime_senzora
        self.max_vrijednost = max_vrijednost
        self.min_vrijednost = min_vrijednost
        self.mjerna_jedinica = mjerna_jednica
        self.value = 0

    def generiraj_vrijednost(self):
        return randint(self.min_vrijednost, self.max_vrijednost)

    def dohvati_podatke(self):
        self.value = self.generiraj_vrijednost()
        return {
            "ime": self.name,
            "vrijednost": self.value,
            "mjerna_jedinica": self.mjerna_jedinica
        }

senzor_temperature = SensorZaRaspberryPi(
    ime_senzora="TEMPERATURA", max_vrijednost=180, min_vrijednost=-40, mjerna_jednica="°C"
)
print(senzor_temperature.dohvati_podatke())
print()

senzor_tlaka = SensorZaRaspberryPi(
    ime_senzora="TLAK", max_vrijednost=1300, min_vrijednost=900, mjerna_jednica="hPa"
)


senzor_vlage = SensorZaRaspberryPi(
    ime_senzora="VLAGA", max_vrijednost=100, min_vrijednost=0, mjerna_jednica="%"
)
raspberry_pi = Jagodica([senzor_temperature, senzor_tlaka, senzor_vlage])
"""
for x in range(3):
    # tu je provjera jel radi dinamičko generiranje podataka
    print(raspberry_pi.get_data())

# ZADATAK: dinamički na zahtjev korisnika (dodati gumb na UI) 
# ponovno pozvati metodu za dohvat podataka sa raspberry pi simulatora

# ZADATAK : usporediti podatke dobivene iz 3 senzora:
# senzor za temperaturu, senozor za vlagu i senzor za tlak
# koje smo spremili u raspberry_pi simulator
# sa podacima koje smo dobili iz prognoze
# primjer podataka iz prognoze:
podaci_iz_prognoze = {
    "2023-03-02T21:00": {
        "TEMPERATURA": 23,
        "TLAK": 1015.3,
        "VLAGA": 54
    }
}

"""