from main import Environment, load_plugins
import time

drom = Environment()
load_plugins(drom)
time.sleep(1)
# text = drom.get_text()
# print('lol')
drom.get_voice('weather')
print('kok')
time.sleep(0.2)
