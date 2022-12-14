while True:
    
    # Napravite aplikaciju za prikaz tablice množenja.
    # Korisnik treba moći unijeti do kojeg broja će se prikazivati tablica.

    do_koliko = int(input("Unesite broj do kojeg želite ispisati tablicu množenja: "))
    if do_koliko > 10:
        print("Ne znam množiti do toliko, pokušaj ponovo!")
        continue

    print('', end='\t')
    broj = 1
    while broj <= do_koliko:
        print(broj, end='\t')
        broj += 1
    print()
    
    broj = 1
    while broj <= do_koliko:
        mnozimo_sa = 1
        print(broj, end='\t')
        while mnozimo_sa <= do_koliko:
            print(broj*mnozimo_sa, end='\t')
            mnozimo_sa += 1
        print()
        broj += 1
        

    # Pravimo se da su korisnici fer i da će uvijek unijeti 1 ili 0
    odgovor = int(input('Želite li prekinuti izvršavanje programa? (Da=1/Ne=0) '))
    if odgovor == 1:
        print('\nViše nema potencijalno beskonačne WHILE petlje s True uvjetom.\n Upravo je završila :-) \n\n')
        break
    elif odgovor == 0:
        continue
    else:
        print("?????")


print("Program je gotov.")