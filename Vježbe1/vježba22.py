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

niz_rijeci = "Pero je Python Programer"
pozicija = 0

while pozicija < len(niz_rijeci):
    if niz_rijeci[pozicija] == 'h':
        break
    print(niz_rijeci[pozicija], end=' ')
    pozicija += 1
print()

while True:
    odgovor = input("Koliko je 2+2?")
    if odgovor == "4":
        print("Bravo")
        break
    else:
        print("Pokušaj ponovno!")
print()

while True:
    try:
        odgovor = int(input("Koliko je 2+2?"))
    except ValueError:
        print('Molim Vas da unesete cijeli broj')
        continue
    if odgovor == 4:
        print("Bravo!")
    else:
        print("Pokušaj ponovno!")
print()"""

niz_rijeci = "Pero je Python Programer"
pozicija = -1
duljina_niza = len(niz_rijeci)

while pozicija < duljina_niza:
    pozicija += 1

    if pozicija == duljina_niza:
        break
    elif niz_rijeci[pozicija] == 'P':
        continue
    print(niz_rijeci[pozicija], end=' ')

print()


niz_rijeci = "Pero je Python Programer"
pozicija = -1
duljina_niza = len(niz_rijeci)

while pozicija < duljina_niza:
    pozicija += 1

    if pozicija == duljina_niza:
        break
    elif niz_rijeci[pozicija].lower() in ['a', 'p']:
        continue
    else:
        pass
    print(niz_rijeci[pozicija], end=' ')

print()