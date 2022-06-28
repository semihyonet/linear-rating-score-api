import json

# Reads file and returns a func that iterates through records
def file_read(filename : str):
    # TODO: Check if file exists

    json_file = open(filename, "r")
    data = json.loads(json_file.read())

    index = 0


    def iterate_json() -> (dict, bool):

        nonlocal index
        if index == len(data):
            return {}, False

        obj = data[index]
        index += 1

        return obj, True

    return iterate_json


review_importer = file_read("../reviews.json")
accommodation_importer = file_read("../accommodations.json")

