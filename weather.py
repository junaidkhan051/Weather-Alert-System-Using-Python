"""
weather.py  –  Alert logic for the Weather Alert System.
"""
from dataclasses import dataclass
@dataclass
class WeatherAlert:
    level: str        # "danger" | "warning" | "info" | "success"
    emoji: str
    title: str
    message: str

def get_alert(temperature_c: int, humidity_pct: int = 50, wind_kph: int = 0) -> WeatherAlert:
    """Return the most relevant WeatherAlert for the given conditions."""

    # --- Extreme heat ---
    if temperature_c >= 42:
        return WeatherAlert(
            level="danger",
            emoji="🔥",
            title="Extreme Heat Warning",
            message="Dangerous heat levels! Avoid outdoor activity, stay cool and hydrated.",
        )
    if temperature_c >= 35:
        return WeatherAlert(
            level="warning",
            emoji="☀️",
            title="High Temperature Alert",
            message="Very hot outside. Drink plenty of water and avoid direct sun.",
        )

    # --- Extreme cold ---
    if temperature_c <= -10:
        return WeatherAlert(
            level="danger",
            emoji="🥶",
            title="Severe Cold Warning",
            message="Dangerously cold! Risk of frostbite. Stay indoors if possible.",
        )
    if temperature_c < 10:
        return WeatherAlert(
            level="warning",
            emoji="🧥",
            title="Cold Weather Alert",
            message="Cold conditions. Wear warm clothes and layers.",
        )

    # --- High wind ---
    if wind_kph >= 70:
        return WeatherAlert(
            level="warning",
            emoji="💨",
            title="Strong Wind Advisory",
            message="High wind speeds. Secure loose objects and be careful outdoors.",
        )

    # --- High humidity ---
    if humidity_pct >= 85 and temperature_c >= 28:
        return WeatherAlert(
            level="info",
            emoji="💧",
            title="High Humidity Notice",
            message="Humid and warm. Feels hotter than the actual temperature.",
        )

    # --- All clear ---
    return WeatherAlert(
        level="success",
        emoji="✅",
        title="Weather is Normal",
        message="Conditions are comfortable. Enjoy your day!",
    )