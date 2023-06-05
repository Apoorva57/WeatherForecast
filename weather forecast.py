import requests
import json
import sys

#API Key
API_KEY = "50fe52c3c30d15d2b7759369d6fc0e04"  

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("Error: ", response.status_code)
        return None
    

def parse_weather(weather_data):
    city = weather_data["name"]
    country = weather_data["sys"]["country"]
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    description = weather_data["weather"][0]["description"]
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']



    print(f"Current weather in {city}, {country}:")
    print(f"Weather description: {description}")
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} km/h")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        city = sys.argv[1]
    else:
        city = input("Enter city name: ")

    weather_data = get_weather(city)
    parse_weather(weather_data)

