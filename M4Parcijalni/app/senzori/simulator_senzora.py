from zajednicko.rezultat_mjerenja import RezultatMjerenja
from random import randint


class Jagodica:
    def __init__(self, senzori):
        self.senzori = senzori
    
    def get_data(self):
        data = []
        for senzor in self.senzori:
            data.append(senzor.dohvati_podatke())
        return data

    def get_data_with_class(self):
        data = []
        for senzor in self.senzori:
            data.append(senzor.dohvati_podatke_u_klasu())
        return data

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
        # ZADATAK: tu koristiti klasu za vraćanje, a ne dict
        return {
            "ime": self.name,
            "vrijednost": self.value,
            "mjerna_jedinica": self.mjerna_jedinica
        }
    
    def dohvati_podatke_u_klasu(self):
        self.value = self.generiraj_vrijednost()
        return RezultatMjerenja(
            vrijednost=self.value,
            mjerna_jedinica=self.mjerna_jedinica,
            tip=self.name
        )

senzor_temperature = SensorZaRaspberryPi(
    ime_senzora="TEMPERATURA", max_vrijednost=180, min_vrijednost=-40, mjerna_jednica="°C"
)

senzor_tlaka = SensorZaRaspberryPi(
    ime_senzora="TLAK", max_vrijednost=1300, min_vrijednost=900, mjerna_jednica="hPa"
)

senzor_vlage = SensorZaRaspberryPi(
    ime_senzora="VLAGA", max_vrijednost=100, min_vrijednost=0, mjerna_jednica="%"
)
raspberry_pi = Jagodica([senzor_temperature, senzor_tlaka, senzor_vlage])
