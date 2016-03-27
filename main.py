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

from kivy.uix.textinput import TextInput

class MainWidget(BoxLayout):
    pass


class AlarmApp(App):
    def __init__(self,**kwargs):
        super(AlarmApp,self).__init__(**kwargs)
        self.clock = None
        self.sound_stop = False
        
        #data_dir = getattr(self, 'user_data_dir')
        
        self.sound = SoundLoader.load('sounds/3.wav')

    def build(self):
        root = MainWidget()
        self.root = root
        return self.root     
        
    def alarm(self,value=0):
        self.sound.play()
        
    def start_alert(self,value=0):
        if self.clock is not None:
            self.clock.cancel()
        self.clock = Clock.schedule_interval(self.check_alert,10)
    
    def stop_alert(self,dt=0):
        if self.clock is not None:
            self.clock.cancel()

    def check_alert(self,dt=0):
        dt = list(time.localtime())
        h = dt[3]
        m = dt[4]
        ht = int(self.root.input_hour.text)
        mt = int(self.root.input_minute.text)
        if h== ht and m >= mt and m < mt + 10 :
            self.sound.volume = 0
            Clock.schedule_interval(self.change_volume,30)
            self.alarm()
            
    def change_volume(self,dt):        
        if self.sound.volume < 1:
            self.sound.volume += 0.1
                
if __name__ == '__main__':
    AlarmApp().run()