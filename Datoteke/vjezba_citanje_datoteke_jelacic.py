ime_datoteke = "vjezba_json_ban_jelacic.csv"

for ime_datoteke in ["vjezba_json_ban_jelacic.csv"]:
    with open(ime_datoteke, "r") as datoteka_u_kojoj_citamo:
        print(f"{ime_datoteke} čitamo: ")
        linije = datoteka_u_kojoj_citamo.readlines()
        for linija in linije:
            print(linija.rstrip())