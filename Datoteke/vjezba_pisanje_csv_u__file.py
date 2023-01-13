vrijednosti_za_upis = {
    "Ime": "Josip",
    "Godina": 1801,
    "Jezici": [
        "Hrvatski",
        "Njemački"
    ]
}

ime_datoteke = "vjezba_json_ban_jelacic.csv"

with open(ime_datoteke, "r") as datoteka_u_koju_pisemo:
    print(f"{ime_datoteke} punimo sadržaj: ")
    for key, value in vrijednosti_za_upis.items():
        string_koji_cemo_pisati = f'{key},{value}\n'
        print(string_koji_cemo_pisati)
        datoteka_u_koju_pisemo.write(string_koji_cemo_pisati)