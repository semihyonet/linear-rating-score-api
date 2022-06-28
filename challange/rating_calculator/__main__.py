from data_import import setup_django_orm
from rating_calculator.initator import calculate_reviews_job


def main():
    calculate_reviews_job(1)

if __name__ == "__main__":
    main()

