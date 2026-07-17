import requests
from dotenv import load_dotenv
import os
import sys
import argparse

# Define constants
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

load_dotenv()


# --- DATA FETCHING FUNCTION ---
def get_weather_data(city, api_key):
    """
    Fetches weather data from the OpenWeatherMap API for a given city.
    """
    request_url = f"{BASE_URL}?q={city}&appid={api_key}"

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
        return weather_info

    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 401:
            print("Error: Invalid API Key. Please check your OPENWEATHER_API_KEY.")
        elif http_err.response.status_code == 404:
            print(f"Error: City not found. Please check the spelling of '{city}'.")
        else:
            print(f"An API error occurred: {http_err}")
        sys.exit(1)

    except requests.exceptions.RequestException as e:
        print("Network error: Could not connect to the weather service.")
        print(f"Details: {e}")
        sys.exit(1)


# --- PRESENTATION FUNCTION ---
def display_weather_data(data):
    """
    Formats and prints the weather data to the console.
    """
    print()
    print(f"Weather in {data['city']}:")
    print("-" * 20)
    print(f"Temperature: {data['temperature']}K")
    print(f"Humidity: {data['humidity']}%")
    print(f"Conditions: {data['description'].capitalize()}")
    print()


# --- MAIN ORCHESTRATION FUNCTION ---
def main():
    """
    The main function to run the weather CLI tool.
    """
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    CITY = "London"

    weather_data = get_weather_data(CITY, API_KEY)

    if weather_data:
        display_weather_data(weather_data)


if __name__ == "__main__":
    main()