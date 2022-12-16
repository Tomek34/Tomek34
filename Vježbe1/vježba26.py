do_koliko_mnozimo = int(input("Do kojeg broja želiš ispisati tablicu množenja?: "))

broj = 1
while broj <= do_koliko_mnozimo:
    print(broj)
    broj += 1
print("While je gotov")


# Tablica množenja

broj = 1
# Ispiši prvi red tablice množenja.
print('\t', end='')
while broj <= do_koliko_mnozimo:
    print(broj, end='\t')
    broj += 1
# Ispišimo tablicu.
print()
# Ponovno inicijaliziraj broj, inače krećemo od 5.
broj = 0
while broj < 5:
    # Ispiši prvi stupac.
    print(broj, end='\t')
    # Ispiši umnožak za svaki stupac.
    for množitelj in range(1, 5):
        print(broj*množitelj, end='\t')
    broj +=1
    # Kreni sa sljedećim redom.
    print()
# Kraj tablice množenja.
print()


odgovor = 1
while odgovor != 1:
    # Dio za provjeru želimo li izaći iz programa.
    odgovor = int(input('Želite li prekinuti izvršavanje programa? (Da=1, Ne=0)'))
    print(odgovor)


"""broj = 1
print('\t', end='')
while broj < 5:
    print(broj, end='\t')
    broj += 1
print()


mnozimo_sa = 1
while mnozimo_sa < 5:
    print(broj*mnozimo_sa, end='\t')
    mnozimo_sa += 1

broj +=1
print()"""