import os
import pathlib
import json

def ispisi_json(data):
    putanja_do_ovog_filea = pathlib.Path(__file__)

    # zeko traži potočić
    project_folder = putanja_do_ovog_filea.parent.parent.parent
    
    data_folder = project_folder.joinpath('ispis')
    print(data_folder.absolute())
    print(data_folder.exists())

    print(json.dumps(data, indent=4))
    datoteka_za_spremanje = "pero.json"
    putanja_do_datoteke = data_folder.joinpath(datoteka_za_spremanje)

    # samo spremanje jsona u datoteku
    with open(putanja_do_datoteke.absolute(), "w", encoding="utf-8") as izlazna_datoteka:
        json.dump(data, izlazna_datoteka, indent=4)