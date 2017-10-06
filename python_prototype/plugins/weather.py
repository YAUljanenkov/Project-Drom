from environment import Plugin
import requests
from pygame import mixer
import time


class Weather(Plugin):

    city = 'Moscow'
    lang = 'ru'
    appid = '9ca00a20c7acd5dde60318507af7bdbb'
    name = 'Weather plugin'
    commands = ['weather for today', 'weather', 'what is the weather like today', "is it raining", 'were they', 'were there', 'were they']

    def on_load(self):
        print('weather plugin enabled')

    def on_command(self, cmd):
        # try:
        #     res = requests.get("http://api.openweathermap.org/data/2.5/weather",
        #                        params={'id': self.city, 'units': 'metric', 'lang': self.lang, 'APPID': self.appid})
        #     data = res.json()
        #     print("conditions:", data['weather'][0]['description'])
        #     print("temp:", data['main']['temp'])
        #     print("temp_min:", data['main']['temp_min'])
        #     print("temp_max:", data['main']['temp_max'])
            mixer.init()
            mixer.music.load('mp3/weather.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.sleep(0.2)
        #     return data['main']['temp'] + 'градусов'
        # except Exception as e:
        #     print("Exception (weather):", e)
        #     pass
