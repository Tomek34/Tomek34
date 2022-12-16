"""niz = "sa 'dvostrukim' navodnicima"
niz_sa_jednostrukim_navodnicima = 'evo i ovakav, u kojem mogu biti i "drugi navodnici" he he'
print(niz)
print(niz_sa_jednostrukim_navodnicima)


niz = niz + niz_sa_jednostrukim_navodnicima
print(niz)


niz_sa_trostrukim_navodnicima = ""pero pero pero""
print(niz_sa_trostrukim_navodnicima)


niz_4 = "pero" + niz
print(niz_4)


ulaz = input("unesi broj ")
ulaz_float = float(ulaz)
ulaz_int = int(round(ulaz_float, 0))
print(ulaz_float)
print(ulaz_int)


ime = "Tomislav"
prezime = "Lončarić"
puno_ime = "Puno ime i prezime je: {} {}".format(ime, prezime)
print(puno_ime)


puno_ime_2 = f"Puno ime i prezime je: {ime} {prezime}"
print(puno_ime_2)


print("\n\tprimjer sa tabom")
print(f'\n\ttata', ime)


godina_rodjenja = 1988
drzava_rodjenja = "Hrvatska"

print(f"\tPuno ime i prezime je: {ime} {prezime}. \n\tGodina rođenja je: {godina_rodjenja}. \n\tDržava rođenja je: {drzava_rodjenja}")

print(f"Moje ime i prezime je: {ime} {prezime}, rođen sam godine: {godina_rodjenja}, u državi: {drzava_rodjenja}")
"""