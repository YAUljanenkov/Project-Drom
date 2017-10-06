import speech_recognition as sr
from pygame import mixer
import time
from gtts import gTTS
import os
import sys

k = 0
def load_plugins(drome):
    global k
    ss = set(os.listdir('plugins')) # Получаем список плагинов в /plugins
    sys.path.insert(0, 'plugins')  # Добавляем папку плагинов в $PATH, чтобы __import__ мог их загрузить

    for s in ss:
        if s != '__pycache__':
            print('Found plugin: ', s)
            __import__(os.path.splitext(s)[0], None, None, [''])
    print(Plugin)# Импортируем исходник плагина
    for plugin in Plugin.__subclasses__():  # так как Plugin произведен от object, мы используем __subclasses__, чтобы найти все плагины, произведенные от этого класса
        p = plugin()  # Создаем экземпляр
        drome.plugins.append(p)
        p.on_load()


class Environment:  # TODO сделать красивую архитектуру, а не как сейчас

    def __init__(self):
        self.r = sr.Recognizer()
        self.plugins = []


    def get_text(self):

        with sr.Microphone() as source:
            print("Say something!")
            mixer.init()
            mixer.music.load('mp3/listening.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.sleep(0.2)
            audio = self.r.listen(source)
        try:
            text = self.r.recognize_google(audio)
            print(text)
        except sr.UnknownValueError:
            text = None
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            try:
                text = self.r.recognize_sphinx(audio)
                print(text)
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
                text = None
            except sr.RequestError as e:
                text = None
                print("Sphinx error; {0}".format(e))
        return text

    def get_voice(self, text):
        if text is not None:
            if text in ['hello home', 'home', 'hello']:
                mixer.init()
                mixer.music.load('mp3/hello.mp3')
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.2)
                return
            elif text in ['who are you', 'are you', 'you', 'what is your name', 'your name']:
                mixer.init()
                mixer.music.load('mp3/whoami.mp3')
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.2)
                return
            else:
                for plugin in self.plugins:
                    if text in plugin.commands:
                        new_text = plugin.on_command(text)
                        if new_text is not None:
                            tts = gTTS(text=new_text, lang='ru', slow=True)
                            tts.save('plugin/1.mp3')
                            mixer.init()
                            mixer.music.load('mp3/1.mp3')
                            mixer.music.play()
                            while mixer.music.get_busy():
                                time.sleep(0.2)
                    else:
                        mixer.init()
                        mixer.music.load('mp3/dont_understand.mp3')
                        mixer.music.play()
                        while mixer.music.get_busy():
                            time.sleep(0.2)
                        return
        else:
            mixer.init()
            mixer.music.load('mp3/dont_understand.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.sleep(0.2)
            return


# Базовый класс плагина
class Plugin(object):
    name = 'undefined'
    commands = []
    # Методы обратной связи
    def on_load(self):
        pass

    def on_command(self, cmd):
        pass


