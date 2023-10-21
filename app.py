from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenWeather API key
api_key ='90d867e92938b8d7bb17f61c4b4e060f'

# Define the endpoint for the OpenWeather API
base_url = 'http://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid{api_key}'

@app.route('/', methods=['GET', 'POST'])
def index():
    city = request.args.get('city') or 'YourDefaultCity'

    if request.method == 'POST':
        city = request.form['city']

    # Set up the query parameters for the OpenWeather API request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }

    # Make a GET request to the OpenWeather API
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        forecast_list = data.get('list')
        if forecast_list:
            return render_template('weather.html', city=city, weather_data=forecast_list)
        else:
            return render_template('weather.html', city=city, weather_data=None)
    else:
        return render_template('weather.html', city=city, weather_data=None)

if __name__ == '__main__':
    app.run(debug=True)
