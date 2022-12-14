rijec = input("Unesi riječ za koju misliš da je palindrom: ")

lista_slova_1 = []
lista_slova_2 = []

pozicija = 0
while pozicija < len(rijec):
    lista_slova_1.append(rijec[pozicija])
    pozicija +=1

lista_slova_2 = lista_slova_1[::-1]
if lista_slova_1 == lista_slova_2:
    print(f'Riječ {rijec} je palindrom.')
else:
    print(f'Riječ {rijec} nije plaindrom.')


pozicija = 0
pola_rijeci = len(rijec)//2
duljina_rijeci = len(rijec)
palindrom = True

while pozicija <= pola_rijeci:
    if rijec[pozicija] == rijec[duljina_rijeci-1-pozicija]:
        pozicija += 1
        continue
    else:
        palindrom = False
        break
if palindrom:
    print(f'Riječ {rijec} je palindrom.')
else:
    print(f'Riječ {rijec} nije palindrom.')