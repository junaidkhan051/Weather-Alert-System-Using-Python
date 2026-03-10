"""
scraper.py  –  Weather data fetcher
Uses the free wttr.in JSON API (no API key required).
"""

import urllib.request
import json
def get_weather(city: str = "Karachi") -> dict | None:

    url = f"https://wttr.in/{city.replace(' ', '+')}?format=j1"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())

        current = data["current_condition"][0]
        nearest_area = data["nearest_area"][0]
        area_name = nearest_area["areaName"][0]["value"]
        country = nearest_area["country"][0]["value"]

        return {
            "city": f"{area_name}, {country}",
            "temperature_c": int(current["temp_C"]),
            "feels_like_c": int(current["FeelsLikeC"]),
            "humidity_pct": int(current["humidity"]),
            "wind_kph": int(current["windspeedKmph"]),
            "description": current["weatherDesc"][0]["value"],
            "weather_code": int(current["weatherCode"]),
        }
    except Exception as exc:
        return {"error": str(exc)}