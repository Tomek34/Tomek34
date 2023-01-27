"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Uvod u rad s Tkinter GUI modulom
                    Gumb - BUTTON
"""


# Import tkinter modul
import tkinter as tk


# DIO ZA FUNKCIJE
def click():
    print('Gumb "button_clikc" je kliknut')



root = tk.Tk()
root.title('Algebra - Python Developer')
root.geometry('600x400')

# Dodajmo element Button kojem cemo kao prvi argument navesti parent element - root
# Svojstvo text predstavlja natpis koji zelimo ispisati na gumbu
button = tk.Button(root, text="Gumbek")
# Ako pokrenemo program, necemo vidjeti nista. Nakon sto smo kreirali element, 
# MORAMO definirati kako ce biti pozicioniran unutar svojeg PARENT elementa
# To radimo na tri nacina, koja cemo kasnije opsiati detaljnije, a sada samo koristimo jedan od njih
# Osnovni je pack() koji predstavlja slaganje elemenata vertikalno ili horizontalno.
button.pack()
# Ako sada pokrenemo program, vidjet cemo gumb s tekstom "Gumbek" koji mozemo kliknuti, ali se nista nece dogoditi.
# Dodatno gumb je pozicioniran gore u sredini. To je osnovna pozicija kada koristimo pack() bez argumenata

# Kreirajmo novi gumb koji ce ispisati poruku u konzoli da ste kliknuli na gumb
# Prije nego kreiramo gumb, kreirajmo funkciju koja ce biti pozvana kada kliknemo na gumb
# Funkciju cemo kreirati u dijelu koji smo naveli da je za kreiranje funkcija
# Umjesto da poziciju na ekranu dodamo naknadno, mozemo sve napraviti u jednoj liniji
button_click = tk.Button(root, text="Klikni me!", command=click).pack(padx=10, pady=10)
# Gumb "Klikni me!" ce biti pozicioniran gore u sredini, ali ispod prvog gumba.
# padx i pady predstavljaju padding svojstvo koje sluzi za odvajanje elemenata po x, odnosno y osi
# Ako kliknete na gumb u konzoli ce se pojaviti poruka iz funkcije click()

# Kreirajmo jednu varijablu u koju cemo pohraniti fotografiju
btn_image = tk.PhotoImage(file='python.gif')

button_image = tk.Button(root, text="Gumbek sa slicicom",
                        image = btn_image,
                        compound = tk.LEFT, # Bez ovoga prikazuje se samo slika, nema teksta
                        relief=tk.GROOVE,
                        command = click,
                        state = tk.DISABLED).pack(padx=10, pady=10)


root.mainloop()