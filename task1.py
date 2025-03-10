import requests
URL = "http://api.openweathermap.org/data/2.5/weather"
def find_weather(city_name, api):

    params = {
        'q': city_name,
        'appid': api,
        'units': 'metric'  
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']

        print(f"Погода в городе {city_name}:")
        print(f"Температура: {temperature}°C")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} hPa")
        print(f"Описание: {weather}")
    else:
        print(f"Ошибка при получении данных: {response.status_code}")

if __name__ == "__main__":
    api = "11aec1c9e94743f2a1090814a7beca8a"
    city_name = "London"
    find_weather(city_name, api)