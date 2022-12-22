# VJEŽBA KORIŠTENJA DICTIONARY-a

# Korisničko ime je KLJUČ, sastoji se od imena i prvog znaka prezimena
# Vrijednost je lista koja sadržava redom: ime, prezime, lozinku
# Napisati funkciju koja će provjeriti da li su ispravi korisničko ime i lozinka
# U slučaju da korisnik s korisničkim imenom postoji i njegova lozinka odgovoara unesenoj,
# Ispisati "Slobodan ulaz, {ime}, {prezime}", i vratiti True
# Ako korisnik s korisničkim imenom ne postoji u dictu korisnici 
# Ispisati "Korisnik ne postoji" i vratiti False
# Ako korisnik postoji, ali mu je lozinka neispravna,
# Ispisati "Neispravna lozinka" i vratiti False


korisnici = {"TomislavL": ["Tomislav", "Lončarić", "hgf2015"]}

def pronadji_korisnika(korisnicko_ime):
    #print(korisnici.keys())
    korisnik_pronadjen = False
    for kljuc in korisnici.keys():
        #print(kljuc)
        if kljuc == korisnicko_ime:
            korisnik_pronadjen = True
            break
    # ne smijemo koristiti 'else' jer ćemo prerano izaći iz 'for' petlje
    if korisnik_pronadjen:
        print("Našli smo korisnika.")
        return True
    else:
        print("Korisnik ne postoji.")
        return False

#korisnicko_ime = input("Unesi korisničko ime: ")
#pronadji_korisnika(korisnicko_ime)

def login(korisnicko_ime, lozinka):
    for kljuc in korisnici.keys():
        # korisničko ime pronađeno
        if kljuc == korisnicko_ime:
            # preko ključa dobiti vrijednosti iz dictionarya
            vrijednosti = korisnici[kljuc]
            # elementima liste pristupamo preko indeksa
            ime = vrijednosti[0]
            prezime = vrijednosti[1]
            lozinka_iz_baze = vrijednosti[2]
            # provjerimo sad i lozinku
            if lozinka == lozinka_iz_baze:
                print(f"Slobodan ulaz, {ime}, {prezime}.")
                return True
            else:
                print("Neispravna lozinka.")
                return False
    print("Korisnik ne postoji.")
    return False

# Napraviti funkciju za dodavanje novog korisnika
# Prima korisničko ime, ime, prezime i lozinku
# Uvjeti: 
    # korisničko ime ne smije postojati u dictionaryu
    # lozinka ne smije biti kraća od 10 znakova
# Provjera rada:
    # ispisati ključ i vrijednosti iz dictionarya za novo unesenog korisnika

korisnici = {"Admin": ["Tomislav", "Lončarić", "hgf2015"]}

#korisnici["PeroP"] = ["Pero", "Perić", "0123456789"]

def provjeri_ispravnost_lozinke(lozinka):
    if len(lozinka) >= 10:
        return True
    else:
        return False
def dodaj_korisnika(korisnicko_ime, ime, prezime, lozinka):
    if pronadji_korisnika(korisnicko_ime):
        print("Korisnik već postoji.")
        return False
    if provjeri_ispravnost_lozinke(lozinka):
        korisnici[korisnicko_ime] = [ime, prezime, lozinka]
    else:
        print("Lozinka nije dobra.")
        return False


dodaj_korisnika("PeroP", "Pero", "Perić", "0123456789")

print(korisnici["PeroP"])