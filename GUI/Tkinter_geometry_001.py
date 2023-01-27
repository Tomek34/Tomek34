"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Uvod u rad s Tkinter GUI modulom
                    Tkinter pozicioniranje elemenata unutar prozora
"""


import tkinter as tk


# U prethodnim primjerima smo vidjeli pack() Geometry Manager. Nekada se jako cesto koritio, 
# a danas se sve rjede koristi. Mozda na Internetu ima dosta primjera koji jos uvijek koriste
# pack() Geometry Manager, ali ipak ga treba napustati.


# Drugi Geometry Manager je place() koji definira tocne koordinate pozicije Widgeta
# Odlican je kada treba tocno pozicionirati Widget, ali nije praktican kada terba prozor maksimizirati
# Idemo vidjeti kako radi place() Geometry Manager

# DIO ZA FUNKCIJE


# DIO ZA root ELEMENT
root = tk.Tk()
root.title('Algebra - Python Developer')
root.geometry('600x400')


btn_image = tk.PhotoImage(file='python.gif')

button_image = tk.Button(root, text="Gumbek sa slicicom",
                        image = btn_image,
                        compound = tk.LEFT).place(x=150, y=75)


oznaka = tk.Label(root, text='Drugi broj')
oznaka.place(x=200, y=90)



root.mainloop()