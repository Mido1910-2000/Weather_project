import tkinter as tk
import requests

def search_text():
    # الحصول على قيمة المدخل من Entry
    search_query = entry.get()
    if not search_query:
        return
    
    # Your OpenWeatherMap API Key
    api_key = "ca68f2da19f343cae1a787e2cd729256"

    # URL for current weather data API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={search_query}&appid={api_key}&lang=en&units=metric"

    # Send the request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        
        weather_data = response.json()

        # Extract the relevant weather information
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        pressure = weather_data['main']['pressure']
        
        # Get precipitation data, if available
        precipitation = weather_data.get('rain', {}).get('1h', 0)

        # Update the Labels with the retrieved data
        temp_value_label.config(text=f"{temperature}°C")
        humidity_value_label.config(text=f"{humidity}%")
        wind_speed_value_label.config(text=f"{wind_speed} m/s")
        pressure_value_label.config(text=f"{pressure} hPa")
        precipitation_value_label.config(text=f"{precipitation} mm")
    else:
        # If there's an error (e.g., city not found), show an error message
        temp_value_label.config(text="Error")
        humidity_value_label.config(text="")
        wind_speed_value_label.config(text="")
        pressure_value_label.config(text="")
        precipitation_value_label.config(text="")

# Create the Tkinter window
window = tk.Tk()
window.title("Weather Forecast")
window.geometry("400x300")

# إعدادات التخطيط
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

# عناصر واجهة المستخدم
location_label = tk.Label(window, text="Location:", font=("Arial", 16))
location_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry = tk.Entry(window)
entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

search_button = tk.Button(window, text="Search", command=search_text)
search_button.grid(row=0, column=2, padx=10, pady=5, sticky="e")

#Show weather information
Temperature = tk.Label(window, text="Temperature: ", font=("Arial", 16))
Temperature.grid(row=1, column=0, padx=10, pady=5, sticky="w")
temp_value_label = tk.Label(window, text="...", font=("Arial", 16))
temp_value_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

Humidity = tk.Label(window, text="Humidity: ", font=("Arial", 16))
Humidity.grid(row=2, column=0, padx=10, pady=5, sticky="w")
humidity_value_label = tk.Label(window, text="...", font=("Arial", 16))
humidity_value_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

Wind_speed = tk.Label(window, text="Wind speed: ", font=("Arial", 16))
Wind_speed.grid(row=3, column=0, padx=10, pady=5, sticky="w")
wind_speed_value_label = tk.Label(window, text="...", font=("Arial", 16))
wind_speed_value_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")

Pressure = tk.Label(window, text="Pressure: ", font=("Arial", 16))
Pressure.grid(row=4, column=0, padx=10, pady=5, sticky="w")
pressure_value_label = tk.Label(window, text="...", font=("Arial", 16))
pressure_value_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")

Precipitation = tk.Label(window, text="Precipitation: ", font=("Arial", 16))
Precipitation.grid(row=5, column=0, padx=10, pady=5, sticky="w")
precipitation_value_label = tk.Label(window, text="...", font=("Arial", 16))
precipitation_value_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")

# Keyboard shortcuts
window.bind('<Return>', lambda event: search_text())
# تشغيل التطبيق
window.mainloop()
