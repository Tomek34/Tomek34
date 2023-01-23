import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker

#############
### MODEL ###
#############

Base = declarative_base()

autor_izdavac = db.Table(
    "autor_izdavac",
    Base.metadata,
    db.Column("autor_id", db.Integer, db.ForeignKey("autor.id")),
    db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id")),
)
knjiga_izdavac = db.Table(
    "knjiga_izdavac",
    Base.metadata,
    db.Column("knjiga_id", db.Integer, db.ForeignKey("knjiga.id")),
    db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id")),
)


class Autor(Base):
    __tablename__ = "autor"
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String)
    prezime = db.Column(db.String)

    knjige = relationship("Knjiga", backref=backref("autor"))
    izdavaci = relationship("Izdavac", secondary=autor_izdavac, back_populates="autori")


class Knjiga(Base):
    __tablename__ = "knjiga"
    id = db.Column(db.Integer, primary_key=True)
    autor_id = db.Column(db.Integer, db.ForeignKey("autor.id"))
    naslov = db.Column(db.String)

    izdavaci = relationship(
        "Izdavac", secondary=knjiga_izdavac, back_populates="knjige"
    )


class Izdavac(Base):
    __tablename__ = "izdavac"
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String)

    autori = relationship("Autor", secondary=autor_izdavac, back_populates="izdavaci")
    knjige = relationship("Knjiga", secondary=knjiga_izdavac, back_populates="izdavaci")


#########################
### KORISTENJE MODELA ###
#########################


def get_knjige_po_izdavacu(session, ascending=True):
    """Dohvati listu izdavaca s brojem knjiga koje su izdali"""
    if not isinstance(ascending, bool):
        raise ValueError(f"Vrijednost arg sortiranja nije ispravna: {ascending}")

    sortiraj = db.asc if ascending else db.desc

    return (
        session.query(
            # Dohvati nazive izdavaca i kreiraj novi stupac naziva "ukupno_knjiga"
            # U taj novi stupac dodaj vrijednost koju vrati func(ion) count naslove knjiga
            # koje je izdao Izdavac
            Izdavac.naziv,
            db.func.count(Knjiga.naslov).label("ukupno_knjiga"),
        )
        # Zatim tome dodaj sve knjige ovog Izdavaca
        .join(Izdavac.knjige)
        # Grupiraj po nazivu izdavaca
        .group_by(Izdavac.naziv)
        # Ovisno o ascending argumentu definiraj je li asc ili desc sortiranje
        .order_by(sortiraj("ukupno_knjiga"))  # direction ce biti asc ili desc
    )


def get_autore_po_izdavacu(session, ascending=True):
    """Dohvati listu izdavaca te broj autora cije knjige su izdali"""
    if not isinstance(ascending, bool):
        raise ValueError(f"Vrijednost arg sortiranja nije ispravna: {ascending}")

    sortiraj = db.asc if ascending else db.desc

    return (
        session.query(Izdavac.naziv, db.func.count(Autor.ime).label("ukupno_autora"))
        .join(Izdavac.autori)
        .group_by(Izdavac.naziv)
        .order_by(sortiraj("ukupno_autora"))
    )


def get_autori(session):
    """Dohvati listu autora sortiranih po prezimenu"""
    return session.query(Autor).order_by(Autor.prezime).all()


def add_knjiga(session, ime_autora, naslov_knjige, naziv_izdavaca):
    """Dodaje novu knjigu u bazu"""
    # Rastavi ime_autora na ime i prezime
    # dio _ je naveden bez imena varijable jer taj dio "zanemarujemo"
    ime, _, prezime = ime_autora.partition(" ")

    # Provjeri je li postoji knjiga u bazi. Ne zlimo duplikate
    knjiga = (
        session.query(Knjiga).join(Autor)
        # filtriraj po naslovu knjige
        .filter(Knjiga.naslov == naslov_knjige)
        # filtriraj po imenu AND prezimenu autora
        .filter(db.and_(Autor.ime == ime, Autor.prezime == prezime))
        # filtriraj po nazivu izdavacu
        .filter(Knjiga.izdavaci.any(Izdavac.naziv == naziv_izdavaca))
        # dohvati prvu ili ako nema podesi na None
        .one_or_none()
    )
    # Ako je gornja provjera vratila neki objekt, udi u IF petlju i prekini funkciju
    # A ako knjiga ima vrijednost None, preskoci ovaj return i nastavi dalje
    if knjiga is not None:
        return

    # Kreiraj novi objekt knjiga
    if knjiga is None:
        knjiga = Knjiga(naslov=naslov_knjige)

    # Dohvati autora po imenu i prezimenu
    autor = (
        session.query(Autor)
        .filter(db.and_(Autor.ime == ime, Autor.prezime == prezime))
        .one_or_none()
    )
    # Ako nema takvog autora, kreirajmo ga
    if autor is None:
        autor = Autor(ime=ime, prezime=prezime)
        session.add(autor)

    # Dohvati izdavaca
    izdavac = (
        session.query(Izdavac).filter(Izdavac.naziv == naziv_izdavaca).one_or_none()
    )
    # Ako nema takvog izdavaca kreirajmo ga
    if izdavac is None:
        izdavac = Izdavac(naziv=naziv_izdavaca)
        session.add(izdavac)

    # Podesimo relacije izmedu knjige i autora i izdavaca
    knjiga.autor = autor
    knjiga.izdavaci.append(izdavac)
    session.add(knjiga)

    # Napokon pohranimo knjigu te eventualno nove objekte autora i izdavaca u bazu
    session.commit()


def main():
    """Glavna funkcija - pocetak programa"""
    # Povezimo se s bazom koristeci SQLAlchemy
    db_engine = db.create_engine("sqlite:///sqlalchemy_book_shop.db")

    # Kreiraj bazu po uputama koje su gore navedene
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    # Dohvati broj knjiga izdanih po svakom izdavacu
    knjige_po_izdavacu = get_knjige_po_izdavacu(session, ascending=False)
    for row in knjige_po_izdavacu:
        print(f"Izdavac: {row.naziv}, ukupno knjiga: {row.ukupno_knjiga}")
    print()

    # Dohvati broj autora po svakom izdavacu
    autori_po_izdavacu = get_autore_po_izdavacu(session)
    for row in autori_po_izdavacu:
        print(f"Izdavac: {row.naziv}, ukupno autora: {row.ukupno_autora}")
    print()

    # Dohvati sve autore
    autori = get_autori(session)
    for autor in autori:
        print(f"Autor: {autor.ime} {autor.prezime}")

    # Dodaj novu knjigu
    add_knjiga(
        session,
        ime_autora="Stephen King",
        naslov_knjige="The Stand",
        naziv_izdavaca="Random House",
    )

    nove_knjige = [
        ["Isaac Asimov", "Foundation", "Random House"],
        ["Pearl Buck", "The Good Earth", "Random House"],
        ["Pearl Buck", "The Good Earth", "Simon & Schuster"],
        ["Tom Clancy", "The Hunt For Red October", "Berkley"],
        ["Tom Clancy", "Patriot Games", "Simon & Schuster"],
        ["Stephen King", "It", "Random House"],
        ["Stephen King", "It", "Penguin Random House"],
        ["Stephen King", "Dead Zone", "Random House"],
        ["Stephen King", "The Shining", "Penguin Random House"],
        [
            "John Le Carre",
            "Tinker, Tailor, Soldier, Spy: A George Smiley Novel",
            "Berkley",
        ],
        ["Alex Michaelides", "The Silent Patient", "Simon & Schuster"],
        ["Carol Shaben", "Into The Abyss", "Simon & Schuster"],
    ]
    for knjiga in nove_knjige:
        add_knjiga(
            session,
            ime_autora=knjiga[0],
            naslov_knjige=knjiga[1],
            naziv_izdavaca=knjiga[2],
        )

    # Osvjezi prikaz novim dohvatom podataka o autoru
    autori = get_autori(session)
    for autor in autori:
        print(f"Autor: {autor.ime} {autor.prezime}")


# Ispravan nacin poziva main() funkcije
# ovime se postiže da se kod importa ovog modula ne izvodi ništa
if __name__ == "__main__":
    main()