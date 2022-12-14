"""rijec = 'Programiranje'
for slovo in rijec:
    print(slovo, end=" ")
print('\n\n')
print(rijec[0:2])
print(len(rijec))

suma = 0
for slovo in rijec:
    suma += ord(slovo)

print(suma)

for slovo in rijec:
    suma += ord(slovo)
    ascii_code = ord(slovo)
    suma += ascii_code
    print(ascii_code, end= " ")

#Sve uvučeno na istu razinu je dio iste naredbe.

rijec_2 = 'Programiranje je zabavno'

print(rijec_2.capitalize())
print(rijec_2.title())
print(rijec_2[0])

lista_voca = ["banana", "anananas"]
lista_voca.append("kiwi")
lista_voca[1] = "jagoda"
banana = lista_voca[0]

print(lista_voca)
print(lista_voca[0])
print(lista_voca[0:3:2])
print(lista_voca[0][0:3:2])
print(banana[0], banana[0+2], banana[0+2+2], sep =" ")

index = 0
granica = 3
korak = 2
print(banana[index:granica:korak])
while index < granica:
    print(banana[index], end= " ")
    index = korak
print()
print(index)"""