import argparse
import json
import os
import sys
import time

from dotenv import load_dotenv
import requests

load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CACHE_FILE = "cache.json"
CACHE_DURATION_SECONDS = 600


def get_weather_data(city, api_key, units="metric"):
    """Fetches weather data from the OpenWeatherMap API using a local cache."""

    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            try:
                cache_data = json.load(f)

                if city.lower() in cache_data:
                    city_cache = cache_data[city.lower()]
                    cached_timestamp = city_cache.get("timestamp", 0)

                    # Check if cached data is still valid.
                    if time.time() - cached_timestamp < CACHE_DURATION_SECONDS:
                        print(f"DEBUG: Cache hit for '{city}'. Using cached data.")
                        return city_cache["data"]

                    print(f"DEBUG: Cache for '{city}' is stale.")

            except json.JSONDecodeError:
                print("DEBUG: Cache file is empty or corrupted.")

    print(f"DEBUG: Cache miss or stale data. Making a new API call for '{city}'.")

    request_url = f"{BASE_URL}?q={city}&appid={api_key}&units={units}"

    try:
        response = requests.get(request_url)
        response.raise_for_status()

        data = response.json()

        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
        }

        full_cache = {}

        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                try:
                    full_cache = json.load(f)
                except json.JSONDecodeError:
                    # Ignore an invalid cache and create a new one.
                    pass

        full_cache[city.lower()] = {
            "data": weather_info,
            "timestamp": time.time(),
        }

        with open(CACHE_FILE, "w") as f:
            json.dump(full_cache, f, indent=4)

        print(f"DEBUG: Saved new data for '{city}' to cache.")

        return weather_info

    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 401:
            print("Error: Invalid API Key. Please check your OPENWEATHER_API_KEY.")
        elif http_err.response.status_code == 404:
            print(f"Error: City '{city}' not found. Please check the spelling.")
        else:
            print(f"An API error occurred: {http_err}")
        return None

    except requests.exceptions.RequestException as e:
        print("Network error: Could not connect to the weather service.")
        print(f"Details: {e}")
        return None


def display_weather_data(data, units):
    """Displays weather information."""

    unit_symbol = "°C" if units == "metric" else "°F"

    print()
    print(f"Weather in {data['city']}:")
    print("-" * 20)
    print(f"Temperature: {data['temperature']}{unit_symbol}")
    print(f"Humidity: {data['humidity']}%")
    print(f"Conditions: {data['description'].capitalize()}")
    print()


def main():
    """Runs the weather CLI application."""

    parser = argparse.ArgumentParser(
        description="Get the current weather for a specific city."
    )

    parser.add_argument(
        "city",
        help="The name of the city to get the weather for.",
    )

    parser.add_argument(
        "--units",
        choices=["metric", "imperial"],
        default="metric",
        help="Temperature units (metric=Celsius, imperial=Fahrenheit).",
    )

    args = parser.parse_args()

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        print("Error: OPENWEATHER_API_KEY not found.")
        print("Add the following to your .env file:")
        print("OPENWEATHER_API_KEY=your_api_key_here")
        sys.exit(1)

    weather_data = get_weather_data(args.city, api_key, args.units)

    if weather_data:
        display_weather_data(weather_data, args.units)


if __name__ == "__main__":
    main()