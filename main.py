import dotenv
import requests



API_KEY =  dotenv.get_key(".env", "API_KEY")
base_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("What City?... \n")
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric",
    "lang": "de"
}

if __name__ == "__main__":
    response = requests.get(base_url, params=params)

    print(response.status_code)
    print(response.text)

    data = response.json()

    temp = data["main"]["temp"]
    weather = data["weather"][0]["main"]
    wind = data["wind"]["speed"]
    humidity = data["main"]["humidity"]

    print(f"Weather: {weather}")
    print(f"Temp:  {int(temp)}C°")
    print(f"Wind: {wind}kph")
    print(f"Humidity: {humidity}%")

