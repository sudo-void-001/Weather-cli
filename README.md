# API-based Weather Fetcher CLI
 
A modern Python command-line application that fetches real-time weather information using the OpenWeatherMap API. The project demonstrates best practices for API integration, command-line interfaces, secure configuration management, local caching, and Python packaging.

------------------------------------

## Features

- 🌤️ Fetches real-time weather information for any city.
- 🌡️ Displays temperature, humidity, and weather conditions.
- 💻 User-friendly command-line interface powered by `argparse`.
- 🌍 Supports both Metric (°C) and Imperial (°F) units.
- 🔐 Secure API key management using environment variables.
- ⚡ Smart local caching (10-minute cache) to reduce unnecessary API requests.
- 📦 Packaged for installation using `pip`.
- 🛡️ Graceful error handling for invalid cities, network issues, and API errors.

----

## Tech Stack

- Python 3
- Requests
- python-dotenv
- argparse
- OpenWeatherMap API
- JSON (Local Cache)

---

## Requirements

- Python 3.10 or later
- An OpenWeatherMap API key

---

## Project Structure

```text
weather_cli/
├── weather.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
└── cache.json        # Generated automatically
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://your-repository-url/weather_cli.git
cd weather_cli
```

### 2. Create a virtual environment

**Linux/macOS**

```bash
python -m venv venv
source venv/bin/activate
```

**Windows**

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install the project

Install the package in editable mode.

```bash
pip install -e .
```

### 4. Create an API key

Obtain a free API key from:

https://openweathermap.org/api

Create a `.env` file in the project root.

```env
OPENWEATHER_API_KEY=your_api_key_here
```

---

## Usage

### Basic Usage

```bash
weather-cli London
```

### Metric Units (°C)

```bash
weather-cli Delhi --units metric
```

### Imperial Units (°F)

```bash
weather-cli "New York" --units imperial
```

---

## Example Output

```text
Weather in London:
--------------------
Temperature: 21°C
Humidity: 64%
Conditions: Broken clouds
```

---

## Caching

The application implements a lightweight local caching system.

- Weather data is cached in `cache.json`.
- Cached entries remain valid for **10 minutes**.
- If cached data is available and valid, the application skips the API request.
- Expired cache entries are automatically refreshed with new data.

This reduces API usage and improves response times.

---

## Error Handling

The application handles common error scenarios, including:

- Invalid API key
- City not found
- Network connectivity issues
- Missing `.env` configuration
- Corrupted or empty cache files

---

## Development

Run the application directly:

```bash
python weather.py London
```

Install in editable mode during development:

```bash
pip install -e .
```

---

## Future Improvements

- Five-day weather forecast
- Weather icons in terminal
- Colored CLI output
- Automatic cache cleanup
- Location detection using IP
- Support for additional weather APIs

---

## License

This project is licensed under the MIT License.

---

## Author

**Rajesh Pattan**

GitHub: https://github.com/sudo-void-001
