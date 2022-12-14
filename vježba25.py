# Napravite aplikaciju za konverziju (u oba smjera):
    # km u milju - (1km = 0.6214 milje)
    # *C u *F - (0*C = 32*F) obrnuto T(*F)=T(*C)*(9/5)+32
    # kg u funtu (pounds) - 1kg = 2.2046 pounds
    # Litra u US galon - 1l = 0.2642 US gal
    # kW (kilowatt) u ks (horsepower ili konjska snaga) - 1 kW = 1.3596ks


"""konverzija_km_u_milju = 0.06214


while True:
    # ALGORITAM
    jedinica = input("Odaberi jedinicu 'km' za kilometre u milje , 'm' za milje u kilometre: ")
    if jedinica == "km":
        duljina = int(input("Unesi broj kilometara: "))
        print(f'{duljina} kilometara je {duljina*konverzija_km_u_milju:.4f} milja.')
    elif jedinica == "m":
        duljina = int(input("Unesi broj milja: "))
        print(f'{duljina} milja je {duljina/konverzija_km_u_milju:.4f} kilometara.')
    else:
        print("Ne znam pretvoriti ovo.")
        continue

    # DIO ZA PROVJERU 
    odgovor = int(input('Želite li prekinuti izvršavanje programa? (Da=1/Ne=0) '))
    if odgovor == 1:
        print('\nViše nema potencijalno beskonačne WHILE petlje s True uvjetom.\n Upravo je završila :-) \n\n')
        break
    else:
        continue
print()"""


"""konverzija_c_u_f = 32

while True:
    jedinica = input("Odaberi jedinicu 'C' za celzijuse u farenheite, 'F' za farenheite u celzijuse: ")
    if jedinica == "C":
        temperatura = int(input("Unesi broj celzijusa: "))
        print(f'{temperatura} u celzijusima je {temperatura*konverzija_c_u_f:.4f} stupnjeva celzijusevih.')"""


"""konverzija_kg_u_funtu = 2.2046

while True:
    jedinica = input("Odaberi jedinicu 'kg' za kilograme u funte, 'p' za funte u kilograme: ")
    if jedinica == "kg":
        kilaža = int(input("Unesi broj kilograma: "))
        print(f'{kilaža} u kilogramima je {kilaža*konverzija_kg_u_funtu:.4f} kilograma.')
    elif jedinica == "p":
        kilaža = int(input("Unesi broj funti: "))
        print(f'{kilaža} u funtama je {kilaža/konverzija_kg_u_funtu:.4f} funti.')
    else:
        print("Ne znam pretvoriti ovo.")
        continue

    odgovor = int(input('Želite li prekinuti izvršavanje programa? (Da=1/Ne=0 '))
    if odgovor == 1:
        print('\nViše nema potencijalno beskonačne WHILE petlje s True uvjetom.\n Upravo je završila :-) \n\n')
        break
    else:
        continue
print()"""


konverzija_litara_u_galon = 0.2642

while True:
    jedinica = input("Odaberi jedinicu 'l' za litre u galone, 'gal' za galone u litre: ")
    if jedinica == "l":
        volumen = int(input("Unesi broj litara: "))
        print(f'{volumen} u litrama je {volumen*konverzija_litara_u_galon:.4} litara.')
    elif jedinica == "gal":
        volumen = int(input("Unesi broj galona: "))
        print(f'{volumen} u galonima je {volumen/konverzija_litara_u_galon:.4} galona.')
    else:
        print("Ne znam pretvoriti ovo.")
        continue

    odgovor = int(input('Želite li prekinuti izvršavanje programa? (Da=1/Ne=0 '))
    if odgovor == 1:
        print('\nViše nema potencijalno beskonačne WHILE petlje s True uvjetom.\n Upravo je završila :-) \n\n')
        break
    else:
        continue
print()