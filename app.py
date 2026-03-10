"""
app.py  –  Weather Alert System (Interactive GUI)
Run with:  streamlit run app.py
"""

import streamlit as st
from scraper import get_weather
from weather import get_alert
import gui

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Weather Alert System",
    page_icon="🌤️",
    layout="centered",
)

gui.apply_custom_styles()

# ── Header ────────────────────────────────────────────────────────────────────
gui.render_header()

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab_live, tab_manual = st.tabs(["🌍  Live Weather Lookup", "🌡️  Manual Check"])


# TAB 1 – Live weather via wttr.in

with tab_live:
    st.markdown("### Search by City")

    col_input, col_btn = st.columns([3, 1])
    with col_input:
        city = st.text_input(
            "City name",
            value="Karachi",
            placeholder="e.g. London, Tokyo, New York…",
            label_visibility="collapsed",
        )
    with col_btn:
        search_clicked = st.button("🔍 Search", key="search_btn")

    if search_clicked or "live_data" not in st.session_state:
        with st.spinner(f"Fetching weather for **{city}**…"):
            data = get_weather(city)
            st.session_state["live_data"] = data
            st.session_state["live_city"] = city

    data = st.session_state.get("live_data")

    if data is None:
        st.error("No data returned. Please try again.")
    elif "error" in data:
        st.error(f"❌ Could not fetch weather: {data['error']}")
    else:
        temp   = data["temperature_c"]
        feels  = data["feels_like_c"]
        humid  = data["humidity_pct"]
        wind   = data["wind_kph"]
        desc   = data["description"]
        c_name = data["city"]

        alert = get_alert(temp, humid, wind)

        gui.render_weather_card(c_name, temp, desc, alert.emoji, feels, humid, wind)
        gui.render_alert_message(alert.level, alert.emoji, alert.title, alert.message)


# TAB 2 – Manual temperature / condition input

with tab_manual:
    st.markdown("### Enter Conditions Manually")

    col1, col2, col3 = st.columns(3)
    with col1:
        m_temp = st.number_input(
            "Temperature (°C)", min_value=-30, max_value=60, value=25, step=1
        )
    with col2:
        m_humid = st.slider("Humidity (%)", 0, 100, 50)
    with col3:
        m_wind = st.slider("Wind (km/h)", 0, 150, 10)

    if st.button("⚡ Check Alert", key="manual_btn"):
        alert = get_alert(m_temp, m_humid, m_wind)

        pct = max(0, min(100, int((m_temp + 30) / 90 * 100)))
        gauge_color = (
            "#ff3c3c" if m_temp >= 35 or m_temp <= -10
            else "#ffa500" if m_temp >= 28 or m_temp < 10
            else "#32cd64"
        )

        gui.render_manual_gauge(m_temp, m_humid, m_wind, gauge_color, pct)
        gui.render_alert_message(alert.level, alert.emoji, alert.title, alert.message)

# ── Footer ────────────────────────────────────────────────────────────────────
gui.render_footer()