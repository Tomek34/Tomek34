# TOK IZVRŠAVANJA KODA

# Često koristimo uvjete kako bismo kontrolirali tijek događaja. Recimo, kada dođete u banku i želite podići neki iznos novaca.
# Ako imate dovoljno na računu i odobren minus, onda ćete dobtii novac, ako nemate,
# dobit ćete ispiriku da nemate dovoljno novaca na računu i da vam ne mogu isplatiti trženi iznos.

#LOGIČKI OPERATORI

# >  Veće od - a je veće od b  a>b
# <  Manje od - a je manje od b  a<b
# ==  Identično - a je identično b  a==b
# !=  Nije identično - a nije identično b  a!=b
# >=  Veće ili identično - a je veće ili identično b  a>=b
# <=  Manje ili identično - a je manje ili identično b  a<=b


"""uvjet = True
if uvjet:
    print("Uvjet je ispunjen")
else:
    print("Uvjet nije ispunjen")


uvijet_za_isplatu = 100 > 200
uvjet_da_ne_isplatimo = 200 < 100

if uvijet_za_isplatu:
    print("Možemo isplatiti")
else:
    print("Ne možemo isplatiti")


uvjet_1 = False
uvjet_2 = False

if uvjet_1:
    print("Možemo isplatiti")
elif uvjet_2:
    print("Ne možemo isplatiti")
else:
    print("Uvjet nije ispunjen")


uvjet_1 = True
uvjet_2 = True
uvjet_3 = True

if uvjet_1:
    print("Možemo isplatiti")
elif uvjet_2:
    print("Ne možemo isplatiti")
elif uvjet_3:
    print("Super Mario")
else:
    print("Uvjet nije ispunjen")"""


brojevi = []
for i in range(1, 31):
    brojevi.append(i)

"""for broj in brojevi:
    if broj % 3 == 0:
        print(f'broj {broj} je djeljiv sa 3')
    elif broj % 6 == 0:
        print(f'broj {broj} je djeljiv sa 6')
    elif broj % 9 == 0:
        print(f'broj {broj} je djeljiv sa 9')
    else:
        print(f'broj {broj} nije djeljiv ni sa 3, ni sa 6, ni sa 9') 
print()


for broj in brojevi:
    if broj % 9 == 0:
        print(f'broj {broj} je djeljiv sa 9')
    if broj % 6 == 0:
        print(f'broj {broj} je djeljiv sa 6')
    if broj % 3 == 0:
        print(f'broj {broj} je djeljiv sa 3')
    else:
        print(f'broj {broj} nije djeljiv ni sa 3, ni sa 6, ni sa 9') 
print()"""