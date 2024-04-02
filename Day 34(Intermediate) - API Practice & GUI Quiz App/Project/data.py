# Getting dynamic questions from the open triva db through API.

import requests

# using parameters to get specific data.
parameters = {
    "amount": 10,
    "type": "boolean",
}
# getting the response from the openTriva DB(API) with parameters.
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  # line to check if there is any error during the response.
data = response.json()  # to convert that data into json format
question_data = data["results"]  # passing that data to our question data
