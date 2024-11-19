import tkinter as tk
import requests

# Function to fetch weather data and update UI
def fetch_weather():
    city = entry.get().strip()
    if not city:
        return

    api_key = "ca68f2da19f343cae1a787e2cd729256"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract weather information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        precipitation = data.get('rain', {}).get('1h', 0)

        # Update UI labels
        update_label(temp_label, f"Temperature: {temperature}°C")
        update_label(humidity_label, f"Humidity: {humidity}%")
        update_label(wind_label, f"Wind Speed: {wind_speed} m/s")
        update_label(pressure_label, f"Pressure: {pressure} hPa")
        update_label(precipitation_label, f"Precipitation: {precipitation} mm")

    except requests.exceptions.RequestException:
        update_label(temp_label, "Error: Could not retrieve data")

# Helper function to update label text
def update_label(label, text):
    label.config(text=text)

# Initialize Tkinter window
window = tk.Tk()
window.title("Weather App")
window.geometry("350x250")

# Input field and search button
tk.Label(window, text="Location:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(window)
entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
tk.Button(window, text="Search", command=fetch_weather).grid(row=0, column=2, padx=10, pady=10)

# Create and display weather info labels
temp_label = tk.Label(window, text="Temperature: ...")
temp_label.grid(row=1, column=0, columnspan=3, sticky="w", padx=10, pady=5)

humidity_label = tk.Label(window, text="Humidity: ...")
humidity_label.grid(row=2, column=0, columnspan=3, sticky="w", padx=10, pady=5)

wind_label = tk.Label(window, text="Wind Speed: ...")
wind_label.grid(row=3, column=0, columnspan=3, sticky="w", padx=10, pady=5)

pressure_label = tk.Label(window, text="Pressure: ...")
pressure_label.grid(row=4, column=0, columnspan=3, sticky="w", padx=10, pady=5)

precipitation_label = tk.Label(window, text="Precipitation: ...")
precipitation_label.grid(row=5, column=0, columnspan=3, sticky="w", padx=10, pady=5)

window.mainloop()
