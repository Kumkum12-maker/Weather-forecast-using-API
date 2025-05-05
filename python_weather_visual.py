import requests
import matplotlib.pyplot as plt
from datetime import datetime

city = input("Enter city name: ")

#Setting up an API
api_key = "9690b5eb0e5ffe55d230b913a699f7f7"
base_url = "https://api.openweathermap.org/data/2.5/"
current_url = f"{base_url}weather?q={city}&appid={api_key}&units=metric"
forecast_url = f"{base_url}forecast?q={city}&appid={api_key}&units=metric"

#Fetching current data
current_response = requests.get(current_url)
if current_response.status_code != 200:
    print("Error fetching current weather. Check city name.")
    exit()

current_data = current_response.json()
print(f"\n--- Current Weather in {city} ---")
print(f"Temperature: {current_data['main']['temp']}°C")
print(f"Humidity: {current_data['main']['humidity']}%")
print(f"Wind Speed: {current_data['wind']['speed']} m/s")
print(f"Weather: {current_data['weather'][0]['description'].title()}")

#Fetching forecasting data
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

temps = []
humidity = []
wind_speed = []
times = []

for entry in forecast_data['list']:
    temps.append(entry['main']['temp'])
    humidity.append(entry['main']['humidity'])
    wind_speed.append(entry['wind']['speed'])
    times.append(datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S'))

#Plotting
plt.figure(figsize=(12, 10))

# Temperature
plt.subplot(3, 1, 1)
plt.plot(times, temps, color='tomato', marker='o')
plt.title(f"5-Day Weather Forecast for {city}")
plt.ylabel("Temperature (°C)")
plt.grid(True)

# Humidity
plt.subplot(3, 1, 2)
plt.plot(times, humidity, color='blue', marker='s')
plt.ylabel("Humidity (%)")
plt.grid(True)

# Wind Speed
plt.subplot(3, 1, 3)
plt.plot(times, wind_speed, color='green', marker='^')
plt.ylabel("Wind Speed (m/s)")
plt.xlabel("Date & Time")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
