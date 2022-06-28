from . import setup_django_orm
from .database_seeder import *
from data_import.database_migration_iniate import  database_migrate

def main():
    database_migrate()
    seed_accommodations()

    seed_reviews()


if __name__ == "__main__":
    main()

