import requests
from datetime import datetime

# Funktion zum Abrufen der Sensordaten von Firebase
def get_sensor_data():
    firebase_url = "https://rasp-68283-default-rtdb.europe-west1.firebasedatabase.app/rasp-data.json"
    firebase_response = requests.get(firebase_url)
    return firebase_response.json()

# public api key
weather_api_key = "7bdc493009ad4931ab585814251301"

# Funktion zum Abrufen der Wetterdaten von WeatherAPI
def get_weather_data(city, days):
   
    weather_url = f"http://api.weatherapi.com/v1/forecast.json?key={weather_api_key}&q={city}&days={days}"
    weather_response = requests.get(weather_url)
    return weather_response.json()

def get_weather_data_with_endpoint(location, date):

    correct_endpoint = "current.json" if (not date or date == datetime.today().strftime('%Y-%m-%d')) else "history.json"
    weather_url = f"http://api.weatherapi.com/v1/{correct_endpoint}"

    if not date:
        return requests.get(weather_url, params={"key": weather_api_key, "q": location, "lang": "de"})
    
    return requests.get(weather_url, params={"key": weather_api_key, "q": location, "dt": date, "lang": "de"})