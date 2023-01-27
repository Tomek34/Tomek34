"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Uvod u rad s Tkinter GUI modulom
                    Predlozak za kreiranje GUI aplikacije
"""


# Import tkinter modul
import tkinter as tk


# DIO ZA FUNKCIJE



# Kod kreiranja grafickog sucelja UVIJEK gradimo hijerahijsku strukturu elemenata
# Prvi element najcesce nazivamo root kao korijen hijerarhije.
# Svaki element MORA imati definiran parent element, IZNIMKA je root koji ima Tk()
# root predstavlja onaj pocetni prozor aplikacije
root = tk.Tk()

# Dodajmo par postavki uz pocetni prozor kao Naslov i pocetnu velicinu sirina x visina
root.title('Pero je super Python Developer!')
root.geometry('800x600')

# DIO ZA DODAVANJE DRUGIH ELEMENATA GUI-a
# Ovdje mozete dodavati druge elemente grafickog sucelja
tk.Button(root, text="KLIKNI ME!").place(x=350, y=250)
# Kada smo dodali sve elemente u graficko sucelje pokrenimo "glavnu petlju", odnosno glavni prozor
root.mainloop()