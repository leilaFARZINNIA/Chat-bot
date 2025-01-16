import requests
from datetime import datetime

# Funktion zum Abrufen der Wetterbedingungen von WeatherAPI
def fetch_weather(location, date=None):
    api_key = "7bdc493009ad4931ab585814251301"  # Ersetzen Sie dies durch Ihren tatsächlichen API-Schlüssel
    base_url = "http://api.weatherapi.com/v1"

    try:
        if not date or date == datetime.today().strftime('%Y-%m-%d'):
            # Aktuelles Wetter abrufen
            endpoint = f"{base_url}/current.json"
            response = requests.get(endpoint, params={"key": api_key, "q": location, "lang": "de"})
        else:
            # Historisches Wetter für ein bestimmtes Datum abrufen
            endpoint = f"{base_url}/history.json"
            response = requests.get(endpoint, params={"key": api_key, "q": location, "dt": date, "lang": "de"})

        # Wetterdaten analysieren und zurückgeben
        if response.status_code == 200:
            weather_data = response.json()
            if "current" in weather_data:
                temp = weather_data['current']['temp_c']
                weather_description = weather_data['current']['condition']['text']
                return f"Das aktuelle Wetter in {location} ist {weather_description} bei einer Temperatur von {temp}°C."
            elif "forecast" in weather_data and "forecastday" in weather_data['forecast']:
                forecast_day = weather_data['forecast']['forecastday'][0]['day']
                temp = forecast_day['avgtemp_c']
                weather_description = forecast_day['condition']['text']
                return f"Das Wetter in {location} am {date} ist {weather_description} mit einer durchschnittlichen Temperatur von {temp}°C."
            else:
                return f"Keine Wetterdaten für {location} am {date} verfügbar."
        else:
            return f"Fehler beim Abrufen der Wetterdaten: {response.status_code}"

    except Exception as e:
        return f"Es ist ein Fehler beim Abrufen der Wetterdaten aufgetreten: {str(e)}"

# Funktion zur Bearbeitung von Benutzeranfragen
def respond_to_user_query(location, event_date=None):
    # Basisantwort für Standortabfrage
    location_response = f"Die Veranstaltung findet in {location} statt."

    # Wetterbedingungen für den Standort und das Datum abrufen
    weather_response = fetch_weather(location, event_date)

    # Antworten kombinieren
    # return f"{location_response} {weather_response}"
    
    return weather_response

# Beispielverwendung
if __name__ == "__main__":
    user_location = "Braunschweig"
    event_date = "2025-01-18"  # Ändern Sie dies auf None für aktuelles Wetter

    response = respond_to_user_query(user_location, event_date)
    print(response)
