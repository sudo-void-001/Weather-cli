# 🌦️ Weather CLI

A simple command-line Python application that fetches real-time weather information using the OpenWeatherMap API.

## Features

- Get current weather by city
- Display temperature
- Display humidity
- Display weather description
- Uses environment variables to securely store the API key

## Tech Stack

- Python 3
- Requests
- Python-dotenv
- OpenWeatherMap API

## Project Structure

```
weather_cli/
├── weather.py
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt
└── venv/
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/weather-cli.git
cd weather-cli
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file

```env
OPENWEATHER_API_KEY=your_api_key_here
```

4. Run the application

```bash
python weather.py
```

## Example Output

```
Weather in London:

Temperature: 297.79
Humidity: 59
Description: clear sky
```

## Requirements

- Python 3.10+
- OpenWeatherMap API Key

## Future Improvements

- User input for city name
- Temperature conversion (Kelvin → Celsius/Fahrenheit)
- Better error handling
- Forecast support
- Colored terminal output

## License

This project is licensed under the MIT License.