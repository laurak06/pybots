import requests
from bs4 import BeautifulSoup


def weather_check():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
    }

    res = requests.get('https://world-weather.ru/pogoda/russia/grozny/?ysclid=m8r97ynkz4885629221', headers=headers)

    sup = BeautifulSoup(res.text, 'lxml')

    timel = sup.find_all('div', class_='hourly-item')
    for time in timel:
        time_el = time.find('span', class_='hourly-item-time').text
        weather = time.find('span', class_='hourly-item-temp').text
        print(time_el)
        print(weather)


weather_check()