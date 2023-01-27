"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Uvod u rad s Tkinter GUI modulom
                    Oznaka - LABEL
"""


import tkinter as tk


# DIO ZA FUNKCIJE
def click():
    # 2. Dodajmo novi tekst u Labelu
    label.config(text='Nova poruka iz funkcije "click"',
                font=('Helvetica', 18),
                fg='red')



# DIO ZA root ELEMENT
root = tk.Tk()
root.title('Algebra - Python Developer')
root.geometry('600x500')


label = tk.Label(root, 
                text="PORUKA",
                # 1. Dodajmo font
                font=('Segoe UI', 16))
label.pack(padx=30, pady=40)

button_click = tk.Button(root, text="Klikni me!", command=click).pack(padx=10, pady=10)


image_in_label = tk.PhotoImage(file='python-logo.png').subsample(7) # Skalira sliku
label_picture = tk.Label(root,
                        text='Tekst u Oznaci',
                        font=('Segoe UI', 20),
                        compound = tk.CENTER,
                        image=image_in_label)
label_picture.pack(padx=5, pady=10)




root.mainloop()