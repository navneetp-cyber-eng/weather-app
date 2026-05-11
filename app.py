import streamlit as st
import requests

st.title("Weather App")

city = st.text_input("Enter city name")

API_KEY = "4454c555f68fdd56c020b7890cef84dc"

if st.button("Search"):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    st.write(data)

    if response.status_code == 200:

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        st.write(f"Temperature: {temperature} °C")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Condition: {condition}")

    else:
        st.write("Error getting weather data")
