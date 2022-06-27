from . import setup_django_orm
from .database_seeder import *


def main():
    seed_accommodations()
    seed_reviews()


if __name__ == "__main__":
    main()

