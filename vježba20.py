tekst = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris '
'nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in '
'reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla '
'pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa '
'qui officia deserunt mollit anim id est laborum. '
'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium '
'doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore '
'veritatis et quasi architecto beatae vitae dicta sunt explicabo. '
'Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, '
'sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. '
'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, '
'adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et '
'dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum '
'exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi '
'consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse '
'quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?'
)

print(tekst, '\n')

tekst = tekst.upper()

print(tekst.count('at'))

"""koliko_puta_se_pojavljuje = 0
trazena_rijec = 'pariatur'.upper()"""

lista_rijeci = tekst.split(' ')

""" for rijec in lista_rijeci:
    ociscena_rijec = rijec.replace('.', '').replace(',', '').replace('?', '')
    if ociscena_rijec == trazena_rijec:
        koliko_puta_se_pojavljuje += 1 

for rijec in lista_rijeci:
    ociscena_rijec = rijec.replace('.', '').replace(',', '').replace('?', '')
    if ociscena_rijec == trazena_rijec:
        koliko_puta_se_pojavljuje += 1 

for rijec in lista_rijeci:
    ociscena_rijec = rijec.replace('.', '').replace(',', '').replace('?', '')
    lista_rijeci[lista_rijeci.index(rijec)] = ociscena_rijec
    if ociscena_rijec == trazena_rijec:
        koliko_puta_se_pojavljuje += 1 



print(f'Riječ {trazena_rijec} se pojavljuje {koliko_puta_se_pojavljuje} puta.')
print(f'Riječ {trazena_rijec} se pojavljuje {lista_rijeci.count(trazena_rijec)} puta.') """

# ZADATAK: prvo iz riječi u listi izbaciti interpunkcijske znakove: , . ? (koristiti 'if' 'elif' 'else')
# traženu riječ dobiti od korisnika (naredba 'input')
# traženu riječ prebaciti u velika slova
# ispisati broj ponavljanja riječi u tekstu na dva načina:
# korištenjem 'for' petlje i 'if' naredbe
# korištenjem 'count' metode nad očišćenom listom

# bonus: kod ispisa koristiti riječ koju je korisnik unio, neizmjenjenu


for rijec in lista_rijeci:
    if '.' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace('.', '')
    elif ',' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace(',', '')
    elif '?' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace('?', '')

original = input("Molim unesite riječ koju želite naći u tekstu: ")
trazena_rijec = original.upper()

koliko_puta_se_pojavljuje = 0

for rijec in lista_rijeci:
    if rijec == trazena_rijec:
        koliko_puta_se_pojavljuje += 1

print(f'Riječ {original} se pojavljuje {koliko_puta_se_pojavljuje} puta.')
print(f'Riječ {original} se pojavljuje {lista_rijeci.count(trazena_rijec)} puta.')