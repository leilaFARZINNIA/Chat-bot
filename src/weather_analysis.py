from datetime import datetime, timedelta

from api.api_call import get_sensor_data, get_weather_data

# Funktion zum Abrufen der Sensordaten von Firebase
def get_local_data():
    
    firebase_data = get_sensor_data()

    # Extrahieren der letzten "n" Sensordaten
    sensor_temperatures = [latest_data['temperature'] for latest_data in list(firebase_data.values())[-3:]]
    timestamps = [latest_data['timestamp'] for latest_data in list(firebase_data.values())[-3:]]
    
    return sensor_temperatures, timestamps

# Funktion zur Analyse von Wetter- und Sensordaten
def analyze_weather(city, days):
    # Sensordaten von Firebase abrufen
    sensor_temperatures, timestamps = get_local_data()

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