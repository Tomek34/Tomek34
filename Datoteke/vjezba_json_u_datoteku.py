import json

vrijednosti_za_upis = {
    "Ime": "Josip",
    "Godina": 1801,
    "Jezici": [
        "Hrvatski",
        "Njemački"
    ]
}

ime_datoteke = "vjezba_json_ban_jelacic.json"

with open(ime_datoteke, "w") as datoteka_u_koju_pisemo:
    print(f"{ime_datoteke} punimo sadržaj: ")
    string_koji_cemo_upisati = json.dumps(vrijednosti_za_upis)
    print(string_koji_cemo_upisati)
    datoteka_u_koju_pisemo.write(string_koji_cemo_upisati)