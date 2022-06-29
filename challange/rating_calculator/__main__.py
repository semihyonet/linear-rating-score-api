from data_import import setup_django_orm
from rating_calculator.initator import calculate_reviews_job


def main():
    reviews = calculate_reviews_job()
    for i in reviews:
        print("\nRatings for accommodation with id {}".format(i), reviews[i])


if __name__ == "__main__":
    main()
    
