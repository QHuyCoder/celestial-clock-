import streamlit as st
from datetime import date
from src.orbit_calc import get_planet_position

st.title("🪐 Celestial Clock - Planet Position Predictor")

planet = st.selectbox("Choose a planet:", ["mars", "venus", "jupiter", "saturn"])
d = st.date_input("Pick a date", date.today())

pos = get_planet_position(planet, d.year, d.month, d.day)

st.subheader("📡 Result:")
st.write(f"RA: {pos['right_ascension']:.2f}h")
st.write(f"Dec: {pos['declination']:.2f}°")
st.write(f"Distance: {pos['distance_km']:.0f} km")

