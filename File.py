from kivy.app import App
from kivy.uix.label import Label
import numpy as np
from kivy.core.audio import SoundLoader

class TestApp(App):

    def sound_on_сircle(self, w, p):
        if p[0] < 100 and p[1] < 100 and self.sound.state=='stop':
            if self.sound:
                self.sound.play()


    #def sound_on_сircle(self, w, p):
    def sound_on(self, w, p):
        if ( ((p[0] - 300)**2 + (p[1]-300)**2) <200**2) and self.sound.state == 'stop':
            if self.sound:
                self.sound.play()

    def sound_off(self,w,p):
        if (((p[0] - 300) ** 2 + (p[1] - 300) ** 2) > 200**2) and self.sound.state == 'play':
        #if (p[0] > 100 or p[1] > 100) and self.sound.state=='play' :
            if self.sound:
                print(self.sound)
                self.sound.stop()


    def build(self):
        from kivy.core.window import Window
        self.sound = SoundLoader.load('sound.mp3')
        self.label = Label()
        print(Window.mouse_pos)
        Window.bind(mouse_pos=lambda w, p: setattr(self.label, 'text', str(p)))
        Window.bind(mouse_pos=self.sound_on)
        Window.bind(mouse_pos=self.sound_off)
        # название объекта
        # название атрибута
        # значение
        # https://pythonz.net/references/named/setattr/

        return self.label





if __name__ == '__main__':
    TestApp().run()