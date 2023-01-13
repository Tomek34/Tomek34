"""try:
    int("1")
except ValueError as e:
    # 'as e' označava naziv greške, odnosno ispisuje grešku kao 'e'
    print(e)
else:
    print("Sve je u redu.")
finally:
    print("Ovo se uvijek izvršava.")"""


"""try:
    # 'r' znači čitanje
    # 'w' znači pisanje
    # 'a' -> ako postoji nastavi pisanje (append), dodavanje na kraj
    # ako ne postoji kreiraj i počni pisati
    # 'rb, wb, ab' znači čitanje/pisanje/append binarnog formata
    datoteka_koju_citamo = open("pero.txt", "r")
    # Metoda rstrip(), koju ima svaki tekstualni tip podataka, se koristi
    # kako bi se uklonio znak '\n' na kraju teksta.
    # 'open' vraća varijablu
except ValueError as e:
    # 'as e' označava naziv greške, odnosno ispisuje grešku kao 'e'
    print(e)
else:
    print("Sve je u redu.")
finally:
    print("Ovo se uvijek izvršava.")
    datoteka_koju_citamo.close()"""


# Tri jednostavna koraka:
# 1. Otvori datoteku za čitanje/pisanje
    # ovaj korak 'zaključava' odnosno onemogućava drugima pristup datoteci
    # kao da smo otvorili konekciju pomoću koje smo se povezali na datoteku
# 2. Pročitaj sadržaj/zapiši tekst
# 3. Zatvori datoteku - ne zaboraviti!
    # ovaj korak osobađa drugim aplikacijama pristup datoteci
    # kao da smo zatvorili konekciju/vezu prema datoteci


"""try:
    datoteka_koju_citamo = open("pero.txt", "r")
    print(datoteka_koju_citamo.readlines())
except ValueError as e:
    print(e)
else:
    print("Sve je u redu.")
finally:
    print("Ovo se uvijek izvršava.")
    datoteka_koju_citamo.close"""

# lakši i kraći način:
koliko_je_uspjelo = 0
# uvijek koristiti lower case, jer radi svugdje
for ime_datoteke in ["pero.txt"]:
    try:
        with open(ime_datoteke, "r") as datoteka_koju_citamo:
            print(f"{ime_datoteke} ima sadržaj: ")
            linije = datoteka_koju_citamo.readlines()
            for linija in linije:
                print(linija.rstrip())
                # ako koristimo 'rstrip' ispisati će i prazan redak između
                print(linija)
            koliko_je_uspjelo += 1
    except FileNotFoundError as err:
        print(err)
        # tu šaljemo poruke o grešci
    finally:
        print(f"Opet smo gotovi. {koliko_je_uspjelo} datoteka smo uspješno obradili.")
        # a tu da smo gotovi UVIJEK!

# OVO JE PRIMJER KAKO NE PISATI KOD!!!
# za petak 13