"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Uvod u rad s Tkinter GUI modulom
                    Tkinter pozicioniranje elemenata unutar prozora
"""


import tkinter as tk


# U prethodnim primjerima smo vidjeli pack() i place () Geometry Manager.
# Sada cemo se upoznati s trecim Geometry Manager grid(). Grid je najlakse opisati kao Excel tabellu
# Widgete pozicionira u celije koje su definirane brojem reda (row = 0) i kolone (column = 0)
# I redovi i kolone pocinju s brojanjem od 0

# DIO ZA FUNKCIJE



# DIO ZA root ELEMENT
root = tk.Tk()
root.title('Algebra - Python Developer')
#root.geometry('600x400')

# Kreirat cemo polje od 3 x 3 elemenata
for i in range(3):

    # BEZ OVOG DIJELA TEST resize
    # Dodajmo mogucnost resize
    root.columnconfigure(i, weight = 1, minsize = 200)
    root.rowconfigure(i, weight = 1, minsize = 200)


    for j in range(3):
        frame = tk.Frame(
            root,
            relief=tk.RAISED,
            borderwidth=2)
        #frame.grid(row=i, column=j)
        frame.grid(row=i, column=j, padx=30, pady=30)
        
        # U svaki frame cemo dodati oznaku - zato oznaka ima parent frame
        label = tk.Label(frame, text=f'Red {i}\nKolona {j}')
        
        # Svaki frame je pozicioniran pomocu grid(), ALI unutar svakog frame Widgeta 
        # pozicioniranjem upravlja pack(). Moguce je kombinirati
        #label.pack()
        label.pack(padx=15, pady=15)

root.mainloop()