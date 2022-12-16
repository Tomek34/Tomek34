# FUNKCIJE

# Skup instrukcija koje su izdvojene u zasebnu cjelinu.
# Instrukcije u funkciji izdvojene su kao i u FOR i WHILE petlji.
# Za pokretanje tih instrukcija vrijede drugačija pravila.
# Funkcije pokrećemo pomoću 'poziva' funkcije ili naziva.
# Namjena funkcija je izdvojiti kod koji se ponavalja u zasebnu cjelinu. Tako dobivamo:
    # Jednom napisani kod možemo koristiti koliko god nam puta treba
    # Održavanje koda je jednostavnije
    # Debbuging je jednostavniji jer nema ponavljanja
# Funkcija bi trebala raditi samo jednu aktivnost.
# Na jednoj strani ima ulaz u koji ubacimo ono što želimo 'obraditi'.
# Mi ne znamo kako funkcija obrađuje ono što smo joj predali (čak nam nije ni bitno).
# Ključna riječ je 'def' za definiranje funkcije, nakon toga ispisujemo ime funkcije.
# Ako funkcija ima 'return' možemo je spremiti u 'varijablu'.
# Funkcije nekon obrade argumenata 'vrate' nekakav rezultat.
# Neke funkcije ne vrate 'ništa', nego samo ispišu poruku o uspjehu ili neuspjehu aktivnosti.
# Svaki programski jezik ima ugrađene funkcije: help(), print(), input(), int(), float(), str(), len()...
# Uz Python se često dodaje 'Batteries included', dakle većinu toga što trebate dolazi u paketu.
# Moduli predstavljaju skup funkcionalnosti koje su izdvojene u zasebnu cjelinu.
# Moduli imaju svoje specifične funkcije. Neki su uključeni odmah, a neke module treba uključiti po potrebi.
# Uključivanje modula se radi na početku 

"""def funkcija_prva():
    print("Funkcija radi.")

for puno_puta in range(10):
    funkcija_prva()
print("Gotovo")

def zbroji_dva_broja(broj_1, broj_2):
    print(f'Zbrojimo dva broja {broj_1} i {broj_2}')
    return broj_1 + broj_2

for x in range(1, 5):
    pero = zbroji_dva_broja(x, x)
    print(pero)

def zbroji_dva_broja(broj_1, broj_2):
    print(f'Zbrojimo dva broja {broj_1} i {broj_2}')
    return broj_1 + broj_2

prvi_broj = 1
drugi_broj = 2
zbroj = zbroji_dva_broja(prvi_broj, drugi_broj)
print(zbroj)

def funkcija_bez_ulaznih_parametara():
    return 100

def primjer_funkcije_koja_nema_rezultat(neki_niz):
    print(f'Unijeli ste "{neki_niz}"')

prvi_broj = 1
drugi_broj = 2

# Funkcija mora biti definirana prije njenog korištenja.

def zbroji_dva_broja(broj_1, broj_2):
    print(f'Zbrojimo dva broja {broj_1} i {broj_2}')
    return broj_1 + broj_2

prvi_broj = 5
drugi_broj = 10
print(zbroji_dva_broja(prvi_broj, drugi_broj))

zbroj = zbroji_dva_broja(100, 200)
prvi_broj = 500
drugi_broj = 100
print(zbroji_dva_broja(prvi_broj, drugi_broj))

for i in range(1, 3):
    print(funkcija_bez_ulaznih_parametara())

izlaz = primjer_funkcije_koja_nema_rezultat('Pero')
print(izlaz)"""

"""def funkcija_broj(broj):
    print(f'{broj} je paran.')

funkcija_broj('10')"""

# Napišite funkciju koja će ispisati 'Pero je najbolji.'

# Ispisivanje funkcije.

"""def funkcija_najbolji(ime):
    print(f'{ime} je najbolji.')

funkcija_najbolji('Tomislav')

# Vraćanje funkcije.

def funkcija_najbolji(ime):
    return f'{ime} je najbolji.'

funkcija_najbolji('Tomislav')"""


"""def moja_funkcija_1(neki_niz, neki_niz_2):
    return f'{neki_niz} - {neki_niz_2}'

prvi_poziv = moja_funkcija_1("Učo", "Soptu")
drugi_poziv = moja_funkcija_1("Klea", prvi_poziv)
print(drugi_poziv)"""


# ZADATAK: napisati funkciju koja prima dva broja i vraća rezultat zbrajanja ta dva broja.
        # Koristeći tu funkciju ispisati rezultat zbrajanja broja 1, 23 i 400

def funkcija_zbrajanje(broj_1, broj_2):
    rezultat = broj_1 + broj_2
    return rezultat

"""prvi_zbroj = funkcija_zbrajanje(1, 23)
drugi_zbroj = funkcija_zbrajanje(prvi_zbroj, 400)
print(drugi_zbroj)

treći_zbroj = funkcija_zbrajanje(drugi_zbroj, 300)
print(treći_zbroj)

četvrti_zbroj = funkcija_zbrajanje(treći_zbroj, 200)
print(četvrti_zbroj)"""