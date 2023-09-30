import requests
import datetime
from flask import Flask, render_template

app = Flask(__name__)

# Settings
api_key = "------"  # API code, enter yours
city = "Warsaw"  # Place to analyze by OpenWeatherMap
units = "metric"  # Choose units

# Weather data importing
def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Generating report
def generate_report():
    weather_data = get_weather()
    if weather_data:
        # Importing time and date
        now = datetime.datetime.now()
        date_time = now.strftime("%A, %d %B %Y %H:%M:%S")

        # Weather data importing
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        return render_template('MainPage.html', date_time=date_time, city=city, description=description, temperature=temperature)
    else:
        return "Error while importing data from API service."

@app.route('/')
def weather_report():
    return generate_report()

if __name__ == '__main__':
    app.run()
