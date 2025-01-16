from datetime import datetime, timedelta

from api.api_call import get_weather_data_with_endpoint

# Funktion zum Abrufen der Wetterbedingungen von WeatherAPI
def fetch_weather(location, date=None):
    try:

        response = get_weather_data_with_endpoint(location, date)

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


def calculate_average_temperature(sensor_data, event_date):

    # Konvertiere das Ereignisdatum in ein datetime-Objekt
    event_day = datetime.strptime(event_date, "%Y-%m-%d")
    three_days_ago = event_day - timedelta(days=3)

    # Filtere die Temperaturmessungen innerhalb der letzten 3 Tage
    temperatures = []
    for record in sensor_data.values():
        record_timestamp = datetime.strptime(record["timestamp"], "%Y-%m-%d %H:%M:%S")
        if three_days_ago.date() <= record_timestamp.date() <= event_day.date():
            temperatures.append(record["temperature"])

    # Berechne die durchschnittliche Temperatur
    if temperatures:
        return sum(temperatures) / len(temperatures)
    else:
        return None
