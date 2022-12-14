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


import random


igrac_1 = "kamen"
igrac_2 = "škare"
igrac_3 = "papir"

izbor_elementa = random(igrac_1, igrac_2, igrac_3)

if igrac_1 > igrac_2:
    print("Igrač 1 je pobjedio.")
else:
    print("Igrač 2 je pobjedio")