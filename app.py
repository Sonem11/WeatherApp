from weather_service import WeatherService
from weather_data import WeatherData

API_KEY = "Your Api Key"  # zameni svojim OpenWeather API ključem

class WeatherApp:
    def __init__(self, api_key):
        self.service = WeatherService(api_key)

    def run(self):
        city = input("Enter city name: ")
        data = self.service.get_weather(city)
        if data:
            weather = WeatherData(
                city=data["name"],
                temperature=data["main"]["temp"],
                description=data["weather"][0]["description"]
            )
            print(weather)

if __name__ == "__main__":
    app = WeatherApp(API_KEY)
    app.run()
