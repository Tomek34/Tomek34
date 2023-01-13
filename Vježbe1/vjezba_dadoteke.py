# Python bez potrebe za instalacijom modula, podržava rad s najvažnijim formatima datoteka.
# Za napredni rad sa specifičnim tipovima datoteka (fotografije, video...). potrebno je instalirati
# specijalizirane besplatne module.
# Prvo ćemo se upoznati s uporabom tekstualnih datoteka (.txt, .json, .log, .ini...).
# Kada to savladamo, krenut ćemo na foto datoteke i njihovu obradu te načine kako prepoznati
# lice jedne ili više osoba na fotografiji.
# Dok pišemo kod koji koristi "vanjske" resurse koji nisu izravno u našem kodu, ne smijemo
# smatrati da ćemo uvijek imati pristup tim resursima.
# Možda na računalu na kojem se izvršava naš kod nemamo prava pristupa željenoj datoteci,
# možda te datoteke ili nema ili možda nemamo prava kreiranja datoteke.
# Možda računalo na kojem se izvršava naš kod nema sljedeće:
        # mrežni pristup do servera na kojem je datoteka koju koristimo ili baza podataka
        # pristup internetu kako bi pristupili resursima u Cloudu
# try: - except: - else: - finally:
# Try: predstavlja blok koda koji želimo izvršiti.
# Except: predstavlja blok koda koji će se izvršiti ukoliko se dogodi neka iznimka kao npr. 
        # nemamo pravo pristupa, nema konekcije na mrežu. Može biti više except blokova.
# Else: ima gotovo istu namjeu kao i Try pa se zato najčešće izostavlja.
# Finally: dio koda koji će se gotovo uvijek izvršiti bez obzira je li se dogodila greška ili je blok uspješno izvršen.
        # Najčeće se dodaje kod, koji će otpustiti zauzete "vanjske" resurse.