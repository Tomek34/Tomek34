import os

from SQLite_repozitorij import (
    create_connection,
    create_employee,
    create_table,
    delete_all_employees,
    delete_employee,
    select_all_employees,
    select_employees_by_id,
    update_employee,
    select_employees_by_email,
)

# drugi način:
# import SQLite_repozitorij

# treći način:
# A BIG NO NO!
# from SQLite_repozitorij import *

def pokreni_aplikaciju():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    sqlite_database_file = "SQLite_Baza_tvrtka.db"

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    """
    db_connection = create_connection(sqlite_database_file)
    if db_connection is None:
        print("Izlazimo")
        return 1
    with db_connection:
        create_table(db_connection, create_table_query)

        #delete_all_employees(db_connection)

        # ZADATAK: umjesto for petlje koristiti korisnički unos kako bi
        # dodali ili promijenili korisnike u bazi

        #djelatnik = ("Pero", "pero@pero.com")
        for djelatnik in [("Pero", "pero@pero.com"), ("Ante", "ante@ante.com")]:
            old_employee_id = select_employees_by_email(db_connection, djelatnik[1])
            print(f"Korisnik sa emailom {djelatnik[1]} ima ID u bazi: {old_employee_id}")
            if old_employee_id is None:
                print(f"Nemamo korisnika {djelatnik}, kreiramo ga.")
                employee_id = create_employee(db_connection, djelatnik)
            else:
                employee_id = old_employee_id
                # djelatnik[1] je tu kako bi se izbjeglo dupliciranje emaila!
                # BONUS zadatak: kako tu isto dodati provjeru ako korisnik slučajno
                # unese email za update koji već imamo.
                djelatnik_za_update = ("Pero Perić", "pero@pero.com", employee_id)
                update_employee(db_connection, djelatnik_za_update)

        select_employees_by_id(db_connection, employee_id)

        #employee_id = create_employee(db_connection, djelatnik)
        #select_employees_by_id(db_connection, employee_id)
        #update_employee(db_connection, djelatnik_za_update)

        select_employees_by_id(db_connection, employee_id)
        #delete_employee(db_connection, employee_id)

        select_employees_by_id(db_connection, employee_id)
        select_all_employees(db_connection)
        
        #delete_all_employees(db_connection)


# ovime se postiže da se kod importa ovog modula ne izvodi ništa
if __name__ == "__main__":
    pokreni_aplikaciju()