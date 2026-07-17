import requests

# Define the core components of our API request as constants.
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
from dotenv import load_dotenv
import os
import sys

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "London"

# Construct the full API request URL.
request_url = f"{BASE_URL}?q={CITY}&appid={API_KEY}"
city_name = CITY  # Store the city name for later use in output.

try:
# Make the API call.
    response = requests.get(request_url)

# Check for a successful response.
    if response.status_code == 200:
    # Parse the JSON data.
        data = response.json()
    
    # Extract the relevant data into descriptive variables.
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

    # Use f-strings to format and print the extracted data.
        print(f"Weather in {city_name}:")
        print("-" * 20)
        print(f"Temperature: {temperature}K")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    else:
    # Print an error message if the request failed.
        print(f"Error: The request failed with status code {response.status_code}")

except requests.exceptions.HTTPError as http_err:
    # Check for specific HTTP status codes to provide tailored error messages.
    if http_err.response.status_code == 401:
        print("Error: Invalid API Key. Please check your API_KEY variable.")
    elif http_err.response.status_code == 404:
        print("Error: City not found. Please check the spelling of the city name.")
    else:
        # For all other 4xx or 5xx errors, print a generic message.
        print(f"An HTTP error occurred: {http_err}")
    sys.exit(1)

except requests.exceptions.RequestException as e:
    # This will catch any network-related errors (e.g., no internet, DNS failure).
    print(f"Network error: Could not connect to the weather service.")
    print(f"Details: {e}")
    # Exit the script with a non-zero status code to indicate an error.
    sys.exit(1)