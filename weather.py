import requests
import json

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'

def get_weather_by_city(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # You can change units to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            # Extract and display weather information
            print(f"Weather in {city_name}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Description: {data['weather'][0]['description']}")
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response")

if _name_ == "_main_":
    city = input("Enter a city name: ")
    get_weather_by_city(city)
