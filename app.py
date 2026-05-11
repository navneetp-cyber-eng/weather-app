import streamlit as st
import requests
st.title("weather App")
city=st.text_input("enter city name")
API_KEY= "4454c555f68fdd56c020b7890cef84dc"
if st.button("search"):
  url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
  response=requests.get(url)
  data=response.json()
  if data["cod"]== 200:
    temperature=data["main"]["temp"]
    humidity=data["main"]["humidity"]
    condition=data["main"][0]["description"]
     st.write(f"Temperature: {temperature} °C")
     st.write(f"Humidity: {humidity}%")
     st.write(f"Condition: {condition}")

    else:
        st.write("City not found")
