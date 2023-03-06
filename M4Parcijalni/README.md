
Napraviti aplikaciju koja će prikazivati podatke dobivene sa senzora i s interneta.

Aplikacija korisniku koji nije ulogiran prikazuje datum, 
grad po vašem odabiru i prognozu za taj grad.

Prognozu dohvatiti sa: Weather Forecast API https://open-meteo.com/
    
Nakon što se korisnik ulogira aplikacija mora prikupiti podatke sa senzora za :
 vlažnost, temperaturu i tlak.

Ovisno o vrijednostima potrebno je naglasiti:
 - prelazi li vrijednost neku maksimalnu vrijednost (npr. temperatura je veća od 23 stupnja C) ili je 
 - vrijednost manja od neke kritične (npr. tlak je ispod 1012 hPa).

Aplikacija ima mogućnost i spremanja podataka u bazu, te ispis podataka u JSON datoteku.


Struktura koda mora biti:

Folder u kojem je aplikacija
   - folder data u kojem će biti baza podataka
   - folder ispis u koji će se spremati izlazna json datoteka
   - folder app u kojem će biti kod podijeljen u module


Također, aplikacija podatke od senzora treba dobiti pozivanjem modula 
RaspberryPi u kojem ćete implementirati klasu koja emulira RaspberryPi i 
vraća podatke sa svih senzora koji su definirani (senzori su isto klase).


class Sensor:
   def dohvati_podatke(self):
      return 5

class Jagodica:

   def __init__(self, sensors):
       self.sensors = sensors

   def get_date(self):
   data = []
   for sensors in self.sensors:
       data.apend(sensor.dohvati_podatke())
   return data
