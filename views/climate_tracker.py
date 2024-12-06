import streamlit as st
import requests
import matplotlib.pyplot as plt

# OpenWeatherMap API key (replace with your actual API key)
API_KEY = "ff6d197f5dd41f81189c6d21f7dadf46"  # Replace with your actual OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather_data(city):
    """Fetches current weather data from OpenWeather API."""
    params = {
        "q": city,
        "appid": "ff6d197f5dd41f81189c6d21f7dadf46",
        "units": "metric"  # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    
    # Check for successful response
    if response.status_code == 200:
        return response.json()  # Return the weather data in JSON format
    else:
        # Show detailed error response from OpenWeather API
        st.error(f"Failed to retrieve weather data: {response.status_code} - {response.json().get('message')}")
        return None


def climate_tracker_page():
    """Displays the Climate Change Tracker page."""

    # --- Page Title ---
    st.title("🌎 Climate Change Tracker")
    st.write("---")

    # --- Introduction ---
    st.subheader("Track Global Climate Trends")
    st.write(
        """
        Use this tool to track real-time weather and climate-related data for various cities around the world.
        Stay informed about current temperature, weather conditions, and climate trends.
        """
    )
    
    # --- City Input ---
    city = st.text_input("Enter a City Name:", value="New York")
    
    # Fetch the weather data when the city is entered
    if city:
        st.write(f"City entered: {city}")  # Debugging line to check the city input
        
        weather_data = fetch_weather_data(city)
        
        if weather_data:
            # Extracting relevant data from the API response
            city_name = weather_data["name"]
            temperature = weather_data["main"]["temp"]
            weather_condition = weather_data["weather"][0]["description"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]
            
            # Display the current weather data
            st.subheader(f"Current Weather in {city_name}:")
            st.write(f"Temperature: {temperature}°C")
            st.write(f"Weather Condition: {weather_condition}")
            st.write(f"Humidity: {humidity}%")
            st.write(f"Wind Speed: {wind_speed} m/s")
            
            # --- Simulated Hourly Temperature Trend Graph ---
            # Here, we'll simulate temperature trend data for illustration (you can replace it with actual data)
            hours = [i for i in range(24)]  # 24 hours of the day
            temperatures = [temperature + (i - 12) * 0.5 for i in hours]  # Simulated hourly temperature changes

            # Create the plot
            fig, ax = plt.subplots()
            ax.plot(hours, temperatures, marker="o", linestyle='-', color='tab:red')
            ax.set_title("Simulated Hourly Temperature Trend (°C)")
            ax.set_xlabel("Hour of the Day")
            ax.set_ylabel("Temperature (°C)")
            ax.set_xticks(hours)
            ax.set_xticklabels([f"{i}:00" for i in hours])
            st.pyplot(fig)
        
        # --- Footer ---
        st.write("---")
        st.write("🔗 Stay updated with the latest climate data and track temperature trends in your region!")
