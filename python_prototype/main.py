from environment import Environment, load_plugins
import time

drom = Environment()
load_plugins(drom)
time.sleep(1)
text = drom.get_text()
drom.get_voice(text)
time.sleep(0.2)
