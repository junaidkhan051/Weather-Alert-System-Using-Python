# Weather Alert System

A Python and Streamlit application that retrieves current weather conditions for a city and presents **rule-based weather alerts** for temperature, humidity, and wind conditions. It also includes a manual mode for testing alert thresholds.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Weather%20Data-wttr.in-0F766E?style=flat-square" alt="wttr.in" />
</p>

## Features

- Search current weather by city
- Display temperature, feels-like temperature, humidity, wind speed, and condition summary
- Rule-based alerts for extreme heat, cold, high wind, and humid conditions
- Manual input mode to test alert behavior
- Dashboard UI with custom styling and visual gauges
- No API key required for the configured `wttr.in` data source

## How It Works

1. The Streamlit interface collects a city name or manual weather inputs.
2. `scraper.py` requests current conditions from the `wttr.in` JSON endpoint.
3. `weather.py` evaluates weather values against configured thresholds.
4. `gui.py` renders the weather card, alert message, and visual presentation.

**Note:** Alerts are based on simple project-defined thresholds. They are educational indicators, not official meteorological warnings or emergency guidance.

## Tech Stack

- Python
- Streamlit
- Python standard library (`urllib`, `json`, `dataclasses`)
- wttr.in current-weather endpoint
- Custom CSS and Streamlit components

## Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/junaidkhan051/Weather-Alert-System-Using-Python.git
   cd Weather-Alert-System-Using-Python
   ```
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   ```
   Windows:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
   macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
3. Install the dependency:
   ```bash
   python -m pip install streamlit
   ```
4. Start the app:
   ```bash
   streamlit run app.py
   ```

Open the local URL printed by Streamlit, usually `http://localhost:8501`.

## Project Structure

```text
Weather-Alert-System-Using-Python/
├── app.py       # Streamlit app and tab orchestration
├── gui.py       # Styles, cards, and gauges
├── weather.py   # Alert rules and alert model
└── scraper.py   # Weather API request and parsing
```

## Roadmap

- Add tests for each alert threshold and boundary condition
- Add request retries, clearer timeout handling, and input validation
- Make alert thresholds configurable and document their rationale
- Add cached requests and graceful API-unavailable states
- Capture real screenshots for the README

## Author

**Junaid Khan** · [GitHub](https://github.com/junaidkhan051) · [LinkedIn](https://www.linkedin.com/in/junaid-khan-46b765319/)
