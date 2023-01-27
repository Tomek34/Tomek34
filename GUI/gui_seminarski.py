import tkinter as tk

# ZADATAK: dodati metodu za provjeru duljine i kompleksnosti lozinke

def provjeri_lozinku(lozinka):
    istina = False

    if len(lozinka) < 8:
        return False
    else:
        for i in lozinka:
            if i.isnumeric():
                istina = True
                break
    
    return istina

class PyFlora:


    def __init__(self):
        # DIO ZA root ELEMENT
        self.root = tk.Tk()
        self.root.title('PyFlora Posuda')
        self.root.geometry('600x400')

        self.nacrtaj_prvi_prozor()
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


    def nacrtaj_prvi_prozor(self):
        self.clear_frame()
        frm_display_username = tk.Frame(self.root).grid(
            column=0, columnspan=3, row=0, rowspan=2, ipadx=20, ipady=20, padx=10, pady=10
        )
        oznaka_username = tk.Label(frm_display_username, text='User name')
        oznaka_username.grid(column=2, row=0, padx=5, pady=5)

        self.username = tk.Entry(frm_display_username, bd=3)
        self.username.grid(column=3, row=0, padx=25, pady=5)

        frm_display_lozinka = tk.Frame(self.root).grid(
            column=0, columnspan=3, row=1, rowspan=2, ipadx=20, ipady=20, padx=10, pady=10
        )
        oznaka_lozinka = tk.Label(frm_display_lozinka, text='Password')
        oznaka_lozinka.grid(column=2, row=1, padx=55, pady=5)

        self.password = tk.Entry(frm_display_lozinka, show="*")
        self.password.grid(column=3, row=1, padx=55, pady=5)

        frm_action_buttons = tk.Frame(self.root).grid(
            column=0, columnspan=3, row=2, ipadx=20, ipady=20, padx=10, pady=10
        )
        button_ulogiraj = tk.Button(frm_action_buttons, text='PRIJAVI ME', command=self.dohvati_podatke)
        button_ulogiraj.grid(column=0, columnspan=3, row=5, ipadx=15, ipady=10, padx=15, pady=10)

    def nacrtaj_drugi_prozor(self):
        self.clear_frame()
        oznaka = tk.Label(self.root, text='Drugi prozor')
        oznaka.grid(column=2, row=0, padx=5, pady=5)
        button_povratak = tk.Button(self.root, text='VRATI ME', command=self.nacrtaj_prvi_prozor)
        button_povratak.grid(column=0, columnspan=3, row=5, ipadx=15, ipady=10, padx=15, pady=10)

    def dohvati_podatke(self):
        print(f"Username: {self.username.get()}")
        print(f"Lozinka: {self.password.get()}")
        if provjeri_lozinku(self.password.get()):
            self.nacrtaj_drugi_prozor()           

    def pokreni(self):
        self.root.mainloop()

        
gui_program = PyFlora()
gui_program.pokreni()