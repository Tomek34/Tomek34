"""for slovo in "Pero je Python Programer":
    if slovo == 'h':
        break
    print(slovo, end=' ')
print()

for slovo in "Pero je Python Programer":
    if slovo == 'P':
        continue
    print(slovo, end=' ')
print()


# Primjer za WHILE/BREAK.

while True:
    print("Ovo nikad neće završiti bez break.")
    zavrsi = input("Jel dosta? ")
    if zavrsi == 'da':
        break
print("Dosta je bilo!")"""


# Igra pogađanje broja između 1 i 100. Napisati program koji će završiti kad korisnik pogodi broj.
# Koristimo algoritam koji smo naučili.
# Ako korisnik unese točan broj, ispiši: "Pogodili ste broj.!" i završite program.
# Ako je korisnik unio broj koji je veći od zadanog broja, ispiši: "Broj je manji".
# Ako je korisnik unio broj koji je manji od zadanog broja, ispiši: "Broj je veći".
# Korisnik može ponovo pogađati.


"""import random


broj_kojeg_pogadjamo = random.randint(1, 100)

print("Pogodi broj između 1 i 100")
while True:
    uneseni_broj = int(input("Unesi broj: "))
    if uneseni_broj == broj_kojeg_pogadjamo:
        print("Pogodili ste! Bravo!")
        break
    if uneseni_broj > broj_kojeg_pogadjamo:
        print("Uneseni broj je veći od traženog.")
    else:
        print("Uneseni broj je manji od traženog.")
print()


broj_kojeg_pogadjamo = random.randint(1, 100)
broj_pokusaja = 1
uneseni_broj = int(input("Unesi broj: "))
while uneseni_broj != broj_kojeg_pogadjamo:
    if uneseni_broj > broj_kojeg_pogadjamo:
        print("Uneseni broj je veći od traženog.")
    else:
        print("Uneseni broj je manji od traženog.")
    uneseni_broj = int(input("Unesi broj: "))
    broj_pokusaja += 1

print(f'Pogodili ste u {broj_pokusaja} pokušaja. Bravo!')"""


# Napraviti program za igru "kamen, škare, papir"

import random

moguci_odabir = ['kamen', 'škare', 'papir']

while True:

    # Kompjuter mora svaki put imati drugi odabir.
    odabir_kompjutera = random.choice(moguci_odabir)

    # Korisnik isto tako svaki put mora unijeti svoj odabir.
    odabir_korisnika = input(f"Odaberi kamen, škare ili papir (kompjuter je odabrao {odabir_kompjutera})")

    if odabir_korisnika == odabir_kompjutera:
        print(f"Oboje ste odabrali {odabir_kompjutera}")
    elif odabir_korisnika == 'kamen' and odabir_kompjutera == 'škare':
        print('Kamen pobjeđuje škare. Pobijedili ste.')
    elif odabir_korisnika == 'kamen' and odabir_kompjutera == 'papir':
        print('Papir pobjeđuje kamen. Izgubili ste.')
    elif odabir_korisnika == 'škare' and odabir_kompjutera == 'kamen':
        print('Kamen pobjeđuje škare. Izgubili ste.')
    elif odabir_korisnika == 'škare' and odabir_kompjutera == 'papir':
        print('Škare pobjeđuju papir. Pobjedili ste.')
    elif odabir_korisnika == 'papir' and odabir_kompjutera == 'škare':
        print('Škare pobjeđuju papir. Izgubili ste.')
    elif odabir_korisnika == 'papir' and odabir_kompjutera == 'kamen':
        print('Papir pobjeđuje kamen. Pobjedili ste.')
    else:
        print("Ovo se ne smije dogoditi!")

    # Dio za provjeru želimo li izaži iz programa:
    odgovor = (input('Želite li prekinuti igru? Unesite DA za prekid, a bilo što drugo za nastavak igre. '))
    if odgovor == 'DA':
        print('Hvala na igranju.')
        break