import aiohttp
import json


async def parse(api):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.openweathermap.org/data/2.5/weather?q=Bishkek&appid={api}&units=metric', ssl=False) as response:
            if response.status == 200:
                data = json.loads(await response.text())
                return (f'Сейчас погода в Бишкеке: {data["main"]["temp"]} градуса\n'
                            f'Ощущается как: {data["main"]["feels_like"]} градуса\n'
                            f'Скорость ветра: {data["wind"]["speed"]}')
            else:
                return 'Нужно ввести реальный город!'