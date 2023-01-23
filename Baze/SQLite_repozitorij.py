"""
REPO KORISTIMO NA NACIN:
    # 1. Definiramo putanju do baze
    database = r"C:\Pytohn\db\TvrtkaDb.db"

    # 2. Kreiramo SQLite3 bazu/konekciju
    db_connection = create_connection(database)

    # 3. Izvrsavamo SQL upite.
    # Koristimo with je tako provjeravamo je li konekcija postoji i na kraju je i zatvorimo
    with db_connection:
        # primjer
        create_table(db_connection, sql_create_table)
"""

# Kao i u bilo kojoj drugoj datoteci, ako trebamo dodatne module, trebamo ih ukljuciti
import sqlite3

### Raspored metoda nema nikakvog utjecaja

# Prva metoda je kreiranje konekcije, odnosno, ako nema baze onda kreiranje nove baze
def create_connection(db_file):
    """
    Kreira konekciju prema SQLite bazi podataka
    Ako baza ne postoji, kreirat ce novu
    :param db_file: Putanja do SQLite db datoteke
    :return: SQLite db connection objekt
    """
    # Kreiramo jednu varijablu i damo joj vrijednost koju cemo vratiti
    db_connection = None

    try:
        # kreiranoj varijabli pokusamo dodijeliti vrijednost i vratimo pozivatelju iz ovog bloka
        db_connection = sqlite3.connect(db_file)
        return db_connection

    except sqlite3.Error as db_error:
        print(db_error)

    # Ako smo dosli do ove linije db_connection i dalje ima vrijednost None i dogodila se neka greska
    return db_connection


# Metoda za kreiranje tabele koja je specificirana u proslijedenom SQL upitu. NE vraca nista
def create_table(db_connection, create_table_sql):
    """ Kreira tabelu definiranu u create_table_sql parametru
    :param db_connection: SQLite db connection objekt
    :param create_table_sql: Tekstualna varijable s CREATE TABLE upitom
    :return:
    """
    try:
        cursor = db_connection.cursor()
        cursor.execute(create_table_sql)

    except sqlite3.Error as db_error:
        print(db_error)


# Metoda za dodavanje zapisa o novom djelatniku u tabelu
def create_employee(db_connection, djelatnik):
    """ Kreira novi red u tabeli Employees na osnovu podataka pohranjenih u djelatnik paramateru tipa tuple
    :param db_connection: SQLite db connection objekt
    :param djelatnik: Tuple s podacima o djelatniku
    :return: id novog retka s podacima o djelatniku
    """
    sq_query = """
        INSERT INTO Employees(name, email)
        VALUES(?, ?) 
    """
    cursor = db_connection.cursor()
    cursor.execute(sq_query, djelatnik)
    db_connection.commit()
    return cursor.lastrowid


# Metoda za azuriranje zapisa o djelatniku u tabeli
def update_employee(db_connection, djelatnik):
    """
    Azurira podtke o Djelatniku
    :param db_connection: SQLite db connection objekt
    :param djelatnik: Tuple s podacima o djelatniku
    :return: None
    """
    sql = """
        UPDATE Employees
        SET name = ? ,
            email = ?
        WHERE id = ?
    """
    cursor = db_connection.cursor()
    cursor.execute(sql, djelatnik)
    db_connection.commit()


# Metoda za brisanje zapisa o djelatniku u tabeli na osnovu ID broja retka
def delete_employee(db_connection, id):
    """
    Brise zapis o djelatniku u tabeli na osnovu ID broja retka
    :param db_connection: SQLite db connection objekt
    :param id: id retka djelatnika
    :return: None
    """
    sql = "DELETE FROM Employees WHERE id=?"
    cursor = db_connection.cursor()
    cursor.execute(sql, (id,))
    db_connection.commit()


# Metoda za brisanje svih zapisa o djelatnicima
def delete_all_employees(db_connection):
    """
    Brise sve zapise o djelatnicima iz tabele
    :param db_connection: SQLite db connection objekt
    :return: None
    """
    sql = "DELETE FROM Employees"
    cursor = db_connection.cursor()
    cursor.execute(sql)
    db_connection.commit()


# Metoda za dohvat svih zapisa o djelatnicima
def select_all_employees(db_connection):
    """
    Dohvaca sve zapise o djelatnicima
    :param db_connection: SQLite db connection objekt
    :return: print redak
    """
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM Employees")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

# Metoda za dohvat zapisa o djelatniku u tabeli na osnovu ID broja retka
def select_employees_by_id(db_connection, id):
    """
    Dohvaca zapise o djelatniku na osnovu ID broja
    :param db_connection: SQLite db connection objekt
    :param id: id retka djelatnika
    :return: id korisnika ako postoji
    """
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT * FROM Employees WHERE id=?", (id,)
    )  # (id,) ZAREZ je OBVEZAN

    # Prethodni SQL upit ce sigurno vratiti SAMO JEDAN redak, ali ovaj nacin pisanja je praktican
    # ako se koristi dohvat po recimo imenu. Tada ce upit vratiti vise readaka.
    rows = cursor.fetchall()


    for row in rows:
        print(row)

# Metoda za dohvat zapisa o djelatniku u tabeli na osnovu ID broja retka
def select_employees_by_email(db_connection, email):
    """
    Dohvaca zapise o djelatniku na osnovu ID broja
    :param db_connection: SQLite db connection objekt
    :param id: id retka djelatnika
    :return: id korisnika ako postoji
    """
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT id FROM Employees WHERE email=?", (email,)
    )  # (email,) ZAREZ je OBVEZAN

    # Prethodni SQL upit ce sigurno vratiti SAMO JEDAN redak, ali ovaj nacin pisanja je praktican
    # ako se koristi dohvat po recimo imenu. Tada ce upit vratiti vise readaka.
    rows = cursor.fetchall()

    employee_id = None
    for row in rows:
        employee_id = row[0]
    return employee_id