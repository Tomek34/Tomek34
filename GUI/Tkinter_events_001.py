"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Uvod u rad s Tkinter GUI modulom
                    Tkinter events - neka aplikacija ozivi
"""


import tkinter as tk


unesena_slova = ''
# DIO ZA FUNKCIJE
# Funkcije koje su vezane uz evente najcesce zovemo handle_nazivEventa ili krace on_nazivEventa
def handle_keypress(event):
    """Ispisi znakove koji je pritisnut na tipkovnici"""    
    print(event.char)
    # 1. Korak
    #label_ispis.config(text=str(event.char))
    # 2. Korak
    global unesena_slova
    unesena_slova += str(event.char)
    label_tekst_var.set(unesena_slova)


# DIO ZA root ELEMENT
root = tk.Tk()
root.title('Algebra - Python Developer')
root.geometry('800x600')

# 2. Korak nastavka - Dodajmo dva elementa Label i neka se u njih ispisuje ono sto korisnik unese
label_tekst_var = tk.StringVar()
label_tekst_var.set('Ovo je mjesto gdje ce se prikazivati unesena slova')

# 1. Korak nastavka - Dodajmo dva elementa Label i neka se u njih ispisuje ono sto korisnik unese
label_naslov = tk.Label(root, text='Key Event', font=('Segoe UI', 18))
label_naslov.grid(column=0, row=0)
#label_ispis = tk.Label(root, text='', font=('Segoe UI', 24), fg='red')

# 2. Korak nastavka
label_ispis = tk.Label(root, textvariable=label_tekst_var, font=('Segoe UI', 24), fg='red')
label_ispis.grid(column=0, row=1)


# Povezi (bind()) event uz tipku (<Key>) uz funkciju handle_keypress()
root.bind("<Key>", handle_keypress)


root.mainloop()