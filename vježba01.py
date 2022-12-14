a = 0
b = 1

if b:
    print("b je True")

if a:
    print("a je True")

ime = "Tomislav"
prezime = "Loncaric"
godina_rodjenja = 1988
drzava_rodjenja = "Hrvatska"
status_radnog_odnosa = "nezaoposlen"


print(
    " Ime korisnika: ",
    ime,
    " Prezime korisnika: ",
    prezime,
    " Godina rođenja: ",
    godina_rodjenja,
    " Država: ",
    drzava_rodjenja,
    " Nezaposlen: ",
    status_radnog_odnosa,
    sep=""
    )

print(
    ime,
    prezime,
    godina_rodjenja,
    drzava_rodjenja,
    status_radnog_odnosa,
)

print(
    "Ime i Prezime korisnika", ime, " ", prezime,
    "\nGodina rođenja:", str(godina_rodjenja)+"."
    "\nDržava:", drzava_rodjenja,
    "\nNeaposlen:", status_radnog_odnosa,
    sep=" "
)

print(
    ime+"\n"+prezime,
)

ime_i_prezime_svako_u_svom_redu = ime+"\n"+prezime
ime_i_prezime_u_jednom_redu = ime+" "+prezime

print(ime_i_prezime_svako_u_svom_redu)
print(ime_i_prezime_u_jednom_redu)

# 3 printa
# korištenje sep

ispis= """
Ime i Prezime: vrijednost varijable ime razmak vrijednost varijable prezime
Godina rođenja: vrijednost varijable godina rođenja i točka odmah iza
Zaposlen: vrijednost varijable zaposlen
"""

print("Ime i Prezime:", ime, prezime)
print("Godina rođenja: ", godina_rodjenja, ".", sep="")
print("Država rođenja:", drzava_rodjenja)
print("Zaposlen:", status_radnog_odnosa)


