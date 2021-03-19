import requests
from datetime import datetime
import config

# My parameters
GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 1.80
AGE = 43

exercise_text = input("Tell me which exercises you did: ")

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": config.APP_ID,
    "x-app-key": config.API_KEY
}
parameters = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}
# Create a query
nutri_create = requests.post(url=NUTRI_ENDPOINT, headers=headers, json=parameters)
nutri_response = nutri_create.json()

SHEETY_ENDPOINT = "https://api.sheety.co/7625988f0e7963473d003ef1ffae377e/apiAiMyWorkouts/workouts"

# Read
sheety_read = requests.get(url=SHEETY_ENDPOINT, headers=config.headers)
print(sheety_read.json())

# Create
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for register in nutri_response["exercises"]:
    sheety_add = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": register["name"].title(),
            "duration": register["duration_min"],
            "calories": register["nf_calories"]

        }
    }

sheety_create = requests.post(url=SHEETY_ENDPOINT, headers= config.headers, json=sheety_add)
print(sheety_create.text)
