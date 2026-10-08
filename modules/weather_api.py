import requests
import re


def extract_city(text):
    """
    Extract city name from a weather command.
    """

    text = text.lower().strip()

    patterns = [
        r"weather in (.+)",
        r"temperature in (.+)",
        r"forecast in (.+)",
        r"weather of (.+)",
        r"temperature of (.+)",
        r"weather for (.+)",
        r"temperature for (.+)"
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

    return None


def get_weather(city):
    """
    Get current weather for a city using Open-Meteo.
    """

    try:

        # Find city coordinates
        geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

        geocoding_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        response = requests.get(
            geocoding_url,
            params=geocoding_params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        if "results" not in data or not data["results"]:
            return f"Sorry, I could not find the city {city}."

        location = data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]

        # Get weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "timezone": "auto"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=15
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()

        current = weather_data["current"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]

        return (
            f"The current temperature in {city_name} is "
            f"{temperature} degrees Celsius. "
            f"Humidity is {humidity} percent, "
            f"and wind speed is {wind_speed} kilometers per hour."
        )

    except requests.exceptions.RequestException as e:

        print(f"Weather API error: {e}")

        return "Sorry, I could not connect to the weather service."