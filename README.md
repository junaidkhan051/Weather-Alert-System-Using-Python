🌤️ Weather Alert System

A Python-based interactive Weather Alert System built with Streamlit. It fetches real-time weather data and provides intelligent, severity-based alerts for extreme weather conditions. The application features a beautiful, glassmorphic UI with dynamic gauges and live weather search capabilities.

## ✨ Features
- **🌍 Live Weather Lookup**: Search for any city worldwide to get real-time temperature, humidity, wind speed, and "feels like" metrics.
- **🚨 Intelligent Alerts**: Automated hazard warnings (Extreme Heat, Severe Cold, High Winds, High Humidity) based on current atmospheric conditions.
- **🌡️ Manual Checking System**: Input custom temperature, humidity, and wind speed values to preview alerts, gauge reactions, and test the alerting logic.
- **🎨 Modern & Premium GUI**: A fully responsive, dark-themed gradient interface featuring custom CSS, custom components, and smooth interactive gauges.
- **⚡ Zero Configuration**: Designed to work out of the box without any API keys. It transparently retrieves live weather data using the free `wttr.in` JSON API.

## 🛠️ Project Structure

- `app.py`: The main Streamlit entry point. It orchestrates the tabs, captures user inputs, and ties the modules together.
- `gui.py`: Houses all the custom frontend rendering. It manages the CSS injection, visual glassmorphism cards, alerts, and dynamic gauges.
- `weather.py`: The core domain logic for evaluating weather data and determining appropriate `WeatherAlert` objects based on defined thresholds.
- `scraper.py`: A lightweight data fetcher that executes HTTP requests to the `wttr.in` API and cleanly parses its JSON responses.

## 🚀 Installation & Setup

1. **Clone the repository** (or download the source):
   ```bash
   git clone https://github.com/yourusername/weather-alert-system.git
   cd weather-alert-system
   ```

2. **Install the dependencies**:
   The project primarily utilizes Streamlit. Ensure you have Python 3.8+ installed, then run:
   ```bash
   pip install streamlit
   ```

3. **Run the application**:
   Start the interactive dashboard globally from the project root:
   ```bash
   streamlit run app.py
   ```
   The application will automatically open in your default web browser at `http://localhost:8501`.



## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request if you want to expand the alerting system, refine the UI, or add new data sources.

## 📜 License
This project was initially instantiated for educational context (AI Assignment 01). Feel free to explore, clone, modify, and integrate it into your own learning or professional dashboards without restriction.
