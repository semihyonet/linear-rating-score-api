import rest_framework.exceptions

from api.accommodations.serializers import *
from .file_util import accommodation_importer, review_importer
import datetime
from api.review.serializers import *
from api.accommodations.models import Accommodation
from django.db.models import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from api.logger import function_logger, app_log
from api.review.models import CustomUser


@function_logger
def seed_reviews():
    has_data = True
    while has_data:
        app_log.info("Iteration on while loop")

        data, has_data = review_importer()

        if not has_data:
            app_log.info("Ending Loop")
            return

        user = UserSerializer(data={
            "id_ref": data["user"]["id"],
            "original_name": data["originalUserName"],
            "original_email": data["originalUserEmail"],
            "original_ip": data["originalUserIp"]
        })

        try:
            app_log.info("Trying to create a user.")
            user.is_valid(raise_exception=True)
            user = user.save()
            app_log.info("Created a user with id {}".format(user.id))
        except rest_framework.exceptions.ValidationError as e:
            app_log.error("Validation Error, user already exists! Fetching the User")
            user = CustomUser.objects.filter(id_ref=data["user"]["id"])[0]

        try:
            app_log.info("Getting the related accommodation")

            accommodation = Accommodation.objects.get(id_ref=data["parents"][0]["id"])
        except ObjectDoesNotExist as e:
            app_log.error("Invalid accommodation_id, doesn't exists. Continuing")
            # Skips review if it has an invalid accommodation_id
            continue
        except MultipleObjectsReturned as e:
            app_log.error("Multiple accommodations with the same id_ref exists.")
            accommodation = Accommodation.objects.filter(id_ref=data["parents"][0]["id"])[0]

        review = ReviewSerializer(data={
            "user_id": user.id,
            "accommodation_id": accommodation.id,

            "id_ref": data["id"],

            "general_review": data["ratings"]["general"]["general"],

            "location_review": data["ratings"]["aspects"]["location"],
            "service_review": data["ratings"]["aspects"]["service"],
            "price_quality_review": data["ratings"]["aspects"]["priceQuality"],
            "food_review": data["ratings"]["aspects"]["food"],
            "room_review": data["ratings"]["aspects"]["room"],
            "childFriendly_review": data["ratings"]["aspects"]["childFriendly"],
            "interior_review": data["ratings"]["aspects"]["interior"],
            "size_review": data["ratings"]["aspects"]["size"],
            "activities_review": data["ratings"]["aspects"]["activities"],
            "restaurants_review": data["ratings"]["aspects"]["restaurants"],
            "sanitary_state_review": data["ratings"]["aspects"]["sanitaryState"],
            "accessibility_review": data["ratings"]["aspects"]["accessibility"],
            "nightlife_review": data["ratings"]["aspects"]["nightlife"],
            "culture_review": data["ratings"]["aspects"]["culture"],
            "surrounding_review": data["ratings"]["aspects"]["surrounding"],
            "atmosphere_review": data["ratings"]["aspects"]["atmosphere"],
            "novice_ski_area_review": data["ratings"]["aspects"]["noviceSkiArea"],
            "advanced_ski_area_review": data["ratings"]["aspects"]["advancedSkiArea"],
            "apres_ski_review": data["ratings"]["aspects"]["apresSki"],
            "beach_review": data["ratings"]["aspects"]["beach"],
            "entertainment_review": data["ratings"]["aspects"]["entertainment"],
            "environmental_review": data["ratings"]["aspects"]["environmental"],
            "pool_review": data["ratings"]["aspects"]["pool"],
            "terrace_review": data["ratings"]["aspects"]["terrace"],
            "housing_review": data["ratings"]["aspects"]["housing"],
            "hygiene_review": data["ratings"]["aspects"]["hygiene"],

            'helios_id': data["heliosId"],
            'updated_date': data["updatedDate"],
            'travel_date': datetime.datetime.fromtimestamp(data["travelDate"] / 1000.0),
            'locale': data['locale'],
            'traveledWith': data['traveledWith'],
            "cooperation_import_partner": data["cooperation"]["importPartner"],
            "cooperation_syndication_partner_id": data["cooperation"]["syndicationPartner"]["id"],
            'entry_date': datetime.datetime.fromtimestamp(data["entryDate"] / 1000.0),
            'status_published': data["status"]["published"],
            'status_checked': data["status"]["checked"],
            'status_reason': data["status"]["reason"]
        })
        try:
            review.is_valid(raise_exception=True)
            new_review = review.save()
            app_log.info("Created a new review with id {}".format(new_review.id))
        except MultipleObjectsReturned as e:
            continue
        for lang in data["titles"]:
            review_title = ReviewTitleSerializer(data={
                "title": data["titles"][lang],
                "language": lang,
                "review_id": new_review.id,
            })
            review_title.is_valid()
            review_title.save()

        for lang in data["texts"]:
            review_text = ReviewTextSerializer(data={
                "text": data["texts"][lang],
                "language": lang,
                "review_id": new_review.id,
            })
            review_text.is_valid()
            review_text.save()


@function_logger
def seed_accommodations():
    data = {}
    has_data = True

    while has_data:

        data, has_data = accommodation_importer()

        if not has_data:
            return

        accommodation = AccommodationSerializer(data={
            "vrw_id": data["vrwId"],
            "fallback_name": data["names"]["fallback"],
            "type": data["type"],
            "media_id_ref": data["media"]["id"],
            "geo_coordinate_type": data["geo"]["type"],
            "geo_coordinate_x": data["geo"]["coordinates"][0],
            "geo_coordinate_y": data["geo"]["coordinates"][1],
            "stars": data["stars"],
            "address_street": data["address"]["street"],
            "address_zipcode": data["address"]["zipcode"],
            "contact_phone": data["contactInformation"]["phone"],
            "contact_email": data["contactInformation"]["email"],
            "contact_url": data["contactInformation"]["url"],
            "helios_url": data["heliosUrl"],
            "is_booking_com_block_enabled": data["bookingComBlockEnabled"],
            "is_premium_ad_link_enabled": data["premiumAdlinkEnabled"],
            "owner_id": data["owner"]["id"],
            "status_published": data["status"]["published"],
            "status_checked": data["status"]["checked"],
            "status_reason": data["status"]["reason"],
            "id_ref": data["id"],
            "helios_id": data["heliosId"],
            "updated_date": datetime.datetime.fromtimestamp(data["updatedDate"] / 1000.0),
            "popularity_score": data["popularityScore"]
        })

        try:
            accommodation.is_valid(raise_exception=True)
            accommodation = accommodation.save()
        except rest_framework.exceptions.ValidationError as e:
            continue

        for lang in data["names"]["main"]:
            accommodation_name = AccommodationNamesSerializer(data={
                "name": data["names"]["main"][lang],
                "language": lang,
                "accommodation_id": accommodation.id,
            })
            accommodation_name.is_valid(raise_exception=True)

            accommodation_name = accommodation_name.save()

        if "awards" in data.keys():
            if "winnerYears" in data["awards"].keys():
                for award_year in data["awards"]["winnerYears"]:
                    accommodation_award = AccommodationAwardSerializer(data={
                        "type": "w",
                        "year": award_year,
                        "accommodation_id": accommodation.id,
                    })
                    accommodation_award.is_valid(raise_exception=True)
                    accommodation_award = accommodation_award.save()

            if "recommendedYears" in data["awards"].keys():
                for award_year in data["awards"]["recommendedYears"]:
                    accommodation_award = AccommodationAwardSerializer(data={
                        "type": "r",
                        "year": award_year,
                        "accommodation_id": accommodation.id,
                    })
                    accommodation_award.is_valid(raise_exception=True)

                    accommodation_award = accommodation_award.save()

        for facility_id in data["facilities"]:
            accommodation_facility = AccommodationFacilitySerializer(data={
                "id_ref": facility_id["id"],
                "accommodation_id": accommodation.id,
            })
            accommodation_facility.is_valid(raise_exception=True)

            accommodation_facility = accommodation_facility.save()

        for historical_url_i in range(len(data["heliosHistoricalUrls"])):
            accommodation_historical = HeliosHistoricalUrlSerializer(data={
                "old_url": data["heliosHistoricalUrls"][historical_url_i]["oldUrl"],
                "new_url": data["heliosHistoricalUrls"][historical_url_i]["newUrl"],
                "accommodation_id": accommodation.id,
            })
            accommodation_historical.is_valid(raise_exception=True)
            accommodation_historical.save()

        for parent_id in data["parents"]:
            accommodation_parent = AccommodationParentsSerializer(data={
                "id_ref": parent_id["id"],
                "accommodation_id": accommodation.id,
            })
            accommodation_parent.is_valid(raise_exception=True)
            accommodation_parent.save()
