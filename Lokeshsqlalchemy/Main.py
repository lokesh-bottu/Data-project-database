from create_database import CreateDatabase
from create_table import create_tables
from insert_data import insert_data

def main():
    database_name = "db5"
    CreateDatabase(database_name)
    create_tables(database_name)
    insert_data(database_name)

if __name__ == "__main__":
    main()
