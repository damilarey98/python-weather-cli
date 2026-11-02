# Python Command-Line Weather App

A beginner-friendly Python project that retrieves current weather information for a city using the Open-Meteo API.

## Features

- Search for a city by name.
- Display the current temperature in Celsius.
- Display current wind speed in km/h.
- Handle unknown cities and common request errors.
- Run directly from the command line.

## Requirements

- Python 3.10 or later
- Internet connection

## Setup on Windows

Clone or download this repository, then open PowerShell in the project folder.

Create a virtual environment:

```powershell
py -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required dependency:

```powershell
python -m pip install -r requirements.txt
```

## Usage

Run the app with a city name:

```powershell
python weather.py Lagos
```

Other examples:

```powershell
python weather.py Abuja
python weather.py London
python weather.py New York
```

## Running Automated Tests

This project uses pytest for automated testing.

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run all tests:

```powershell
python -m pytest -v
```

The tests simulate weather API responses, so they do not require live weather API requests.

The test suite checks:
- Successful city coordinate retrieval.
- Handling of unknown cities.
- Handling of API connection failures.
- Successful weather data retrieval.

## APIs

This project uses the free Open-Meteo geocoding API to find city coordinates and the Open-Meteo forecast API to retrieve current weather information.

No API key is required for this basic example.

## Learning objectives

This project demonstrates Python functions, HTTP requests, JSON data, command-line arguments, error handling, virtual environments, and Git/GitHub basics.