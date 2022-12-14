# napišite program u kojem ćete varijablu napuniti sa range naredbom od 100 brojeva korištenjem for petlje
# naredbom copy kopirati novu listu i onda u for petlji ispisivati koliki je broj ponavljanja u toj listi count naredbe

# u varijablu koja se zove 'banana' staviti string "banana"
# korištenjem for petlje proći kroz svako slovo u varijabli banana i ispisati
# slovo i count(slovo) u obliku :
# "Slovo b se u 'banana' pojavljuje 1 put"

naziv_liste = []
for broj in range(0, 101):
    naziv_liste.append(broj)
print(naziv_liste)

nova_lista = naziv_liste.copy()

for element in nova_lista:
    print(f'Element {element} se pojavljuje {nova_lista.count(element)} puta u listi')
print('\n'*4)
banana = 'banana'
for slovo in banana:
    print(f'Slovo {slovo} se u \'{banana}\' pojavljuje {banana.count(slovo)} puta')


print(banana.count("p"))

kopija = naziv_liste.copy

naziv_liste.extend(["p", "e", "r", "o"])
treca_lista = ["p", "e", "r", "o"]
print(naziv_liste)
for x in ["p", "e", "r", "o"]:
    naziv_liste.append(x)
print(naziv_liste)

naziv_liste += treca_lista
naziv_liste.extend(treca_lista)
naziv_liste[len(naziv_liste)-1] = "A"
print(naziv_liste)
print(treca_lista)

naziv_liste.insert(12, "Pero")
naziv_liste.insert(16, "Pero")
print(naziv_liste)
print(naziv_liste.index("Pero", 13))

index_od_pero = naziv_liste.index("Pero")
print(index_od_pero)
print(naziv_liste.index("Pero", index_od_pero))
print(f'Na indexu {index_od_pero} se nalazi {naziv_liste[index_od_pero]}')

#index_od_pero = naziv_liste.index("Pero", index_od_pero+1)


lista_voca = ["banana", "ananans"]
p = [1,2,3,4,5,6,7,8,9,0]
print(lista_voca)
lista_voca.sort()
print(lista_voca)
print(p)
print(f'index od 0 je {p.index(0)}')
p.sort(reverse=True)
print(p)

print(f'index od 0 je {p.index(0)}')
p.sort()
print(f'index od 0 je {p.index(0)}')
p.sort(reverse=True)
print(f'index od 0 je {p.index(0)}')

sortirani_p = sorted(p)
obrnuto_sortirani_p = sorted(p, reverse=True)
print(obrnuto_sortirani_p)

for x in reversed(p):
    print(x, end= ' ')
print()

obrnuti_p = list(reversed(p))
print(obrnuti_p)

print(p)
p.sort()

print(p)
p.sort(reverse=True)

print(p)


obrnuto_sortirani_p = sorted(p, reverse=True)
p.sort(reverse=True)

print(obrnuto_sortirani_p == p)
print(p.clear())
print(obrnuto_sortirani_p == sorted(p, reverse=True))
print(p)