from rating_calculator.algorithms import ln_rating_calculator
from datetime import datetime

from api.review.models import Review
from api.review.serializers import ReviewSerializer

from api.logger import app_log,function_logger

@function_logger
def calculate_reviews_job(accommodation_id= None):
    app_log.info("Creating the calculator")
    calculator = ln_rating_calculator(2, datetime.now())

    if accommodation_id == None:
        app_log.info("Fetching all reviews")
        reviews = Review.objects.all()
    else:
        app_log.info("Only fetching reviews with accommodation_id = {}".format(accommodation_id))
        reviews = Review.objects.filter(accommodation_id=accommodation_id)

    review_serializer = ReviewSerializer(data=reviews, many=True)
    review_serializer.is_valid()

    length = {}
    total = {}
    review_columns = []

    app_log.info("Fetching the columns that indicate a review in Review models attributes")

    for key in review_serializer.data[0].keys():
        if key.endswith("review", 7):
            review_columns.append(key)

    app_log.info("Starting Calculation by iteration")
    # No logs in the loop for performance
    for i in review_serializer.data:
        if i["accommodation_id"] not in total.keys():
            total[i["accommodation_id"]] = {}
            length[i["accommodation_id"]] = {}

        for review_type in review_columns:

            if review_type not in total[i["accommodation_id"]].keys():
                total[i["accommodation_id"]][review_type] = 0
                length[i["accommodation_id"]][review_type] = 0

            if i[review_type] != None:
                year = int(i["entry_date"][:4])
                month = int(i["entry_date"][5:7])
                day = int(i["entry_date"][8:10])

                length[i["accommodation_id"]][review_type] += 1
                total[i["accommodation_id"]][review_type] += calculator(datetime(year, month, day),
                                                                        i[review_type])

    app_log.info("Calculation concluded, parsing the results")

    for id in total:
        for review_type in total[id]:
            if length[id][review_type] != 0:
                total[id][review_type] /= length[id][review_type]

    app_log.info("Returning the results")
    return total
