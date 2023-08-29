import requests
from datetime import datetime

API_ID = "39c8288a"
API_KEY = "5671315fd7a44d284b5df62df63a251a"
exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"
USERNAME = "nemanjagajic"
PASSWORD = "Micro123/"
TOKEN = "sfoiqw98dm23i02d23d"

GENDER = "Male"
WEIGHT = 95.5
HEIGHT = 192.2
AGE = 22

exercise_input = input("Tell me which exercise you did today? :")

headers = {
    "x-app-id":API_ID,
    "x-app-key":API_KEY
}

parameters = {
    "query":exercise_input,
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
}

response = requests.post(url=exercise_endpoint,
                         json=parameters,
                         headers=headers)
result = response.json()
print(result)

sheety_api = "https://api.sheety.co/11d549f99d95b20aed87e1791857516c/workoutsTracking/workouts"

today = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date":today,
            "time":today_time,
            "exercise":exercise['name'].title(),
            "duration":exercise['duration_min'],
            "calories":exercise['nf_calories']
    }
}

bearer_hearder = {
    "Authorization":"Bearer TOKEN"
}

sheety_response = requests.post(url=sheety_api,
                                json=sheety_parameters,
                                headers=bearer_hearder)