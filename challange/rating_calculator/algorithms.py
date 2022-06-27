import datetime
import math


def ln_rating_calculator(active_years: int, current_date_time: datetime.datetime):
    def ln(x):
        return math.log(x, 2)

    # Cache for weight that gets calculated with month
    weight_cache = {}
    # Cache for the calculations, if active_years are passed then month = 0
    active_cache = {}

    current_month = current_date_time.month.real

    active_years = active_years

    inactive_default_weight = ln(1.77)  # ln(1.77)

    def find_weight_with_cache(month) -> float:
        weight = weight_cache.get(month)
        if month == 0:
            return inactive_default_weight
        if weight is None:
            weight = ln(25 - (current_month - month))
            weight_cache[month] = weight

        return weight

    def ln_calculator_with_cache(month, rating):
        if rating not in active_cache.keys():
            active_cache[rating] = {}

        if month not in active_cache[rating].keys():
            weight = find_weight_with_cache(month)
            active_cache[rating][month] = weight * rating

        return active_cache[rating][month]

    def calculate(rating_datetime: datetime.datetime, rating: int):
        if current_date_time.year - active_years >= rating_datetime.year:
            month = 0  # 0 Means it's inactive therefore equal to a set weight
        else:
            month = rating_datetime.month

        return ln_calculator_with_cache(month, rating)

    return calculate
