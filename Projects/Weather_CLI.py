# # 2️⃣ Weather App (CLI)	          requests	        Get weather using free API

import requests

def get_weather(city):
    '''Fetches weather data for a given city using OpenWeatherMap API.'''

    API_Key = input("Enter your API key: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"

    response = requests.get(url)

    data = response.json()
    print(data)
    if response.status_code == 200:
        city_name = data['name']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        sea_level = data['main']['sea_level']
        wind_speed = data['wind']['speed']
        weather = data['weather'][0]['discription']

        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"It feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather}")
        print(f"WindSpeed: {wind_speed} m/s")
        print(f"Sea Level: {sea_level} m")

    else:
        raise Exception(f"Error while fetching data: {data['message']}")
    

city = input("Enter the City whose weather details you want: ")

get_weather(city)

# My API_KEY:
# 04ee89c10c12ffb1a995982bcb9b9445