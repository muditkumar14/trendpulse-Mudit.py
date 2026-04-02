import streamlit as st
import requests
import json
from together import Together

# Set your API key here OR use environment variable
TOGETHER_API_KEY = "your_api_key_here"

client = Together(api_key=TOGETHER_API_KEY)

st.set_page_config(page_title="Weather App", layout="centered")

st.title("🌍 Live Weather App ")
st.write("Get real-time weather")
st.write("Created by Mudit")

# Input field
city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    if city:
        try:
            # Step 1: Get lat/long from AI
            message = f"""
            For the given city, provide the latitude and longitude values in JSON.
            City: {city}.
            Only provide keys: latitude, longitude, current_weather=true.
            """

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[{"role": "user", "content": message}],
                stream=False,
            )

            content = response.choices[0].message.content
            coords = json.loads(content)

            # Step 2: Call weather API
            api_url = "https://api.open-meteo.com/v1/forecast"
            weather_response = requests.get(api_url, params=coords)

            weather_data = weather_response.json()

            # Step 3: Extract weather
            temperature = weather_data['current_weather']['temperature']
            windspeed = weather_data['current_weather']['windspeed']

            # Display result
            st.success(f"📍 City: {city}")
            st.write(f"🌡 Temperature: {temperature}°C")
            st.write(f"💨 Wind Speed: {windspeed} km/h")

        except Exception as e:
            st.error("Something went wrong. Check API response or input.")
            st.write(e)
    else:
        st.warning("Please enter a city name")