import requests

# Define the core components of our API request as constants.
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "London"

# Construct the full API request URL.
request_url = f"{BASE_URL}?q={CITY}&appid={API_KEY}"
city_name = CITY  # Store the city name for later use in output.

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

    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Description: {weather_description}")
else:
    # Print an error message if the request failed.
    print(f"Error: The request failed with status code {response.status_code}")