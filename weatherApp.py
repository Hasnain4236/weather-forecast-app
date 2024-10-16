import os
import requests
from flask import Flask, request, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the OpenWeatherMap API key from environment variables
api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        weather_data = get_weather(city)
    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)