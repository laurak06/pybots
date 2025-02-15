import requests
import json


def parse(city, api):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if response.status_code == 200:
        data = json.loads(response.text)
        return (f'Сейчас погода в {city.title()}: {data["main"]["temp"]} градуса\n'
                    f'Ощущается как: {data["main"]["feels_like"]} градуса\n'
                    f'Скорость ветра: {data["wind"]["speed"]}')
    else:
        return 'Нужно ввести реальный город!'