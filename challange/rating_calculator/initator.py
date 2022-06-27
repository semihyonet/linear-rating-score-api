from rating_calculator.algorithms import ln_rating_calculator
from datetime import datetime

from api.review.models import Review
from api.review.serializers import ReviewSerializer


def initiator():
    calculator = ln_rating_calculator(2, datetime.now())

    reviews = Review.objects.all()
    review_serializer = ReviewSerializer(data=reviews, many=True)
    review_serializer.is_valid()

    length = {}
    total = {}
    review_columns = []

    for key in review_serializer.data[0].keys():
        if key.endswith("review", 7):
            review_columns.append(key)

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

    for id in total:
        for review_type in total[id]:
            if length[id][review_type] != 0:
                total[id][review_type] /= length[id][review_type]


    for i in total:
        print(total[i])
