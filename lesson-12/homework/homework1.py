import requests

def get_api_key():
    return "0cf6fb3714ed3b91a832888c33d5c9f6"  # Replace with your OpenWeatherMap API Key

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": get_api_key(),
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(url, params=params).json()
    
    if response.get("cod") != 200:
        print("Error fetching weather data.")
        return
    
    weather = response["weather"][0]["description"].capitalize()
    temp = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    wind_speed = response["wind"]["speed"]
    
    print(f"Weather in {city}:")
    print(f"Description: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

def main():
    city = input("Enter a city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()