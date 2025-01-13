import requests
from datetime import datetime, timedelta

# Funktion zum Abrufen der Wetterdaten von WeatherAPI
def get_weather_data(city, days):
    weather_api_key = "7bdc493009ad4931ab585814251301"
    weather_url = f"http://api.weatherapi.com/v1/forecast.json?key={weather_api_key}&q={city}&days={days}"

    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    return weather_data

# Funktion zum Abrufen der Sensordaten von Firebase
def get_sensor_data():
    firebase_url = "https://rasp-68283-default-rtdb.europe-west1.firebasedatabase.app/rasp-data.json"
    firebase_response = requests.get(firebase_url)
    firebase_data = firebase_response.json()

    # Extrahieren der letzten "n" Sensordaten
    sensor_temperatures = [latest_data['temperature'] for latest_data in list(firebase_data.values())[-3:]]
    timestamps = [latest_data['timestamp'] for latest_data in list(firebase_data.values())[-3:]]
    
    return sensor_temperatures, timestamps

# Funktion zur Analyse von Wetter- und Sensordaten
def analyze_weather(city, days):
    # Sensordaten von Firebase abrufen
    sensor_temperatures, timestamps = get_sensor_data()

    # Wetterdaten von WeatherAPI abrufen
    weather_data = get_weather_data(city, days)

    # Extrahieren der Vorhersagetemperaturen
    forecast_temperatures = [weather_data['forecast']['forecastday'][i]['day']['avgtemp_c'] for i in range(days)]

    # Berechnung der Temperaturdifferenz und Erstellen der Textausgabe
    output_text = ""
    
    # Berechne das heutige Datum
    today = datetime.today()
    
    for i in range(days):
        sensor_temp = sensor_temperatures[i]
        forecast_temp = forecast_temperatures[i]
        timestamp = timestamps[i]
        
        # Temperaturdifferenz berechnen
        temperature_difference = sensor_temp - forecast_temp
        temperature_difference_str = f"+{temperature_difference:.2f}°C" if temperature_difference > 0 else f"{temperature_difference:.2f}°C"
        
        # Datum für jeden Tag berechnen
        date_for_day = today + timedelta(days=i)
        formatted_date = date_for_day.strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
        
        # Textausgabe für jeden Tag erstellen
        output_text += f"Tag {i+1} ({formatted_date}):\n"
        output_text += f"Vorhersagetemperatur: {forecast_temp}°C\n"
        output_text += f"Reale Temperatur (Sensor): {sensor_temp}°C\n"
        output_text += f"Temperaturdifferenz: {temperature_difference_str} (Die {'reale Temperatur ist höher' if temperature_difference > 0 else 'Vorhersage ist höher'})\n\n"

    # Ergebnis zurückgeben
    return output_text