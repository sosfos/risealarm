import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import Sound, SoundLoader
from kivy.uix.button import Button
from kivy.clock import Clock
import time
from random import random
from os.path import join

class MainWidget(BoxLayout):
    pass


class AlarmApp(App):
    def __init__(self,**kwargs):
        super(AlarmApp,self).__init__(**kwargs)
        self.clock = None
        self.sound_stop = False
        
        #data_dir = getattr(self, 'user_data_dir')
        
        self.sound = SoundLoader.load('sounds/3.mp3')
        
    def build(self):
        return MainWidget()     
        
    def alarm(self,value=0):
        self.sound.play()
        
    def start_alert(self,value=0):
        self.clock = Clock.schedule_interval(self.check_alert,10)

    def check_alert(self,dt):
        dt = list(time.localtime())  
        h = dt[3]
        m = dt[4]
        if h==21 and m<30:
            self.sound.volume = random()
            self.alarm()

                
if __name__ == '__main__':
    AlarmApp().run()