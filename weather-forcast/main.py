# 5fa84b66218ceedbb8a21a7e6321ba9f
import requests

def get_weather_data(city):
    api_key = "fa84b66218ceedbb8a21a7e6321ba9f"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "zip" :city,
        "appid": api_key,
        "units": "metric" 
    }
    # "q": city,
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == 200:
        weather = data["weather"][0]["description"].capitalize()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        print("Weather Forecast")
        print(f"Condition: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found. Please enter a valid city name.")

def main():
    city = input("Enter a city name: ")
    weather_data = get_weather_data(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
