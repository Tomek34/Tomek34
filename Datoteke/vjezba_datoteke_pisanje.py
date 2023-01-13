koliko_je_uspjelo = 0
for ime_datoteke in ["pero_pisanje.txt"]:
    try:
        # 'a' -> dodajemo na kraj datoteke (NE ZNAČI NOVA LINIJA!)
        # 'w' -> destruktivna operacija (obriše pa piše)
        with open(ime_datoteke, "a") as datoteka_u_koju_pisemo:
            print(f"{ime_datoteke} punimo sadržaj: ")
            for linija in range(1, 3):
                string_koji_ide_u_datoteku = (f"Pero je super {linija}\n")
                datoteka_u_koju_pisemo.writelines(string_koji_ide_u_datoteku)
            koliko_je_uspjelo += 1
    except FileNotFoundError as err:
        print(err)
    finally:
        print(f"Opet smo gotovi. {koliko_je_uspjelo} datoteka smo uspješno obradili.")