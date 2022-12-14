# Napravite aplikaciju za konverziju (u oba smjera):
    # km u milju - (1km = 0.6214 milje)
    # *C u *F - (0*C = 32*F) obrnuto T(*F)=T(*C)*(9/5)+32
    # kg u funtu (pounds) - 1kg = 2.2046 pounds
    # Litra u US galon - 1l = 0.2642 US gal
    # kW (kilowatt) u ks (horsepower ili konjska snaga) - 1 kW = 1.3596ks



konverzija = int(input("Unesite broj koji želite konvertirati: "))
duljina_u_kilometrima = konverzija*0.6214
duljina_u_miljama = konverzija*1.609344

if konverzija == duljina_u_kilometrima:
    print(duljina_u_miljama*1.609344)
if konverzija == duljina_u_miljama:
    print(duljina_u_kilometrima*0.6214)