import os
import requests
import datetime as dt

# API credentials from environment variables
API_APP_ID = os.environ.get("NUTRITION_API_APP_ID")
API_KEY = os.environ.get("NUTRITION_API_KEY")
TOKEN = os.environ.get("SHEETY_WORKOUTTRACKING_TOKEN")

# Get current timestamp for logging
now = dt.datetime.now()
time_str = now.strftime("%X")
date_str = now.strftime("%d/%m/%Y")

# API endpoints
nutrition_url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint_url = "https://api.sheety.co/3dca078483aa0eaf6680dc77ee6a3d70/workoutTracking/workouts"

# Headers for Nutritionix API
nutrition_headers = {
    "x-app-id": API_APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# Get workout details from user
nutrition_data = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": 45,
    "height_cm": 170,
    "age": 18,
    "gender": "male"
}

# Send to Nutritionix for parsing
nutrition_response = requests.post(nutrition_url, json=nutrition_data, headers=nutrition_headers)
result = nutrition_response.json()

# Add each exercise to Google Sheets
for exercise in result["exercises"]:
    sheety_data = {
        "workout": {
            "date": date_str,
            "time": time_str,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    sheety_response = requests.post(sheety_endpoint_url, json=sheety_data, headers=sheety_headers)
    print(sheety_response.text)