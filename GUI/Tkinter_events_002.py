"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Uvod u rad s Tkinter GUI modulom
                    Tkinter events - neka aplikacija ozivi
"""


import tkinter as tk


# DIO ZA FUNKCIJE
# Funkcije koje su vezane uz evente najcesce zovemo handle_nazivEventa ili krace on_nazivEventa
def zbroji():
    txt_entry_rezultat.delete(0, tk.END)
    prvi_broj = int(txt_entry_prvi_br.get())
    drugi_broj = int(txt_entry_drugi_br.get())
    rezultat = prvi_broj + drugi_broj
    txt_entry_rezultat.insert(tk.END, str(rezultat))

def handle_btn1_oduzmi(event): # Obavezno proslijediti event argument
    txt_entry_rezultat.delete(0, tk.END)
    prvi_broj = int(txt_entry_prvi_br.get())
    drugi_broj = int(txt_entry_drugi_br.get())
    rezultat = prvi_broj - drugi_broj
    txt_entry_rezultat.insert(tk.END, str(rezultat))



# DIO ZA root ELEMENT
root = tk.Tk()
root.title('Algebra - Python Developer')
root.geometry('600x400')


oznaka_prvi_br = tk.Label(root, text='Prvi broj')
oznaka_prvi_br.grid(column=0, row=0, padx=5, pady=5)
txt_entry_prvi_br = tk.Entry(bd=3)
txt_entry_prvi_br.grid(column=1, row=0, padx=5, pady=5)

oznaka_drugi_br = tk.Label(root, text='Drugi broj')
oznaka_drugi_br.grid(column=0, row=1, padx=5, pady=5)
txt_entry_drugi_br = tk.Entry()
txt_entry_drugi_br.grid(column=1, row=1, padx=5, pady=5)

button_zbroji = tk.Button(root, text='Zbroji', command=zbroji)
button_zbroji.grid(column=0, row=2, padx=5, pady=5)
button_oduzmi = tk.Button(root, text='Oduzmi')
button_oduzmi.grid(column=1, row=2, padx=5, pady=5)
button_oduzmi.bind('<Button-1>', handle_btn1_oduzmi)
    
oznaka_rezultat = tk.Label(root, text='Rezultat')
oznaka_rezultat.grid(column=0, row=3, padx=5, pady=5)
txt_entry_rezultat = tk.Entry()
txt_entry_rezultat.grid(column=1, row=3, padx=5, pady=5)



root.mainloop()