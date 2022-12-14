"""# Tuple koristi ( ) zagrade
# N-terac je kolekcija podatak koju nakon što je kreiramo, NIJE moguće mijenjati.
# Elementi su kao i u listi. samostalni, to znači da nisu u paru kao kod Rječnika.
# Primjena:
    # TUPLE se često koristi kao tip pohrane povezanih podataka unutar neke kolekcije
    # Zato jer je nepromjenjiv koristi se kao ključ u Rječnicima.
    # Recimo podaci o nekoj osobi su pohranjeni u jednu TUPLE kolekciju, a onda su te TUPLE kolekcije pohranjene u neku listu.

# SINTAKSA
# Ako smo za listu koristili [ ] zagrade, za Dictionary { } zagrade, za Tuple ćemo koristiti obične ( ) zagrade.

n_terac = ('Python', 'Algebra', 'Programiranje')

print('\nIspis Tupla\n')
for element in n_terac:
    print(element)
print()


print(n_terac.count("Python"))
prvi_index = n_terac.index("Python")
print(prvi_index)
print(n_terac.index("Python"))
print(n_terac[1:3])
print(len(n_terac))"""