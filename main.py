from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ListProperty, BooleanProperty, DictProperty
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import json

class SoundPlayer(BoxLayout):

    def play_sound(self):
        sound=SoundLoader.load('sound.mp3')
        if sound:
            sound.play()


class PageLayoutExample(BoxLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        acc = ObjectProperty(None)

        self.but=Button(size_hint=(1, 0.1))
        self.add_widget(self.but)
        self.sound = SoundLoader.load('sound.mp3')
        self.img = Image(source='circle_button.png')
        self.sequence = [1,0, 1, 0, 1, 0]
        self.number = 0
        self.answers = []
        self.current_answer = None
        self.saved=None #only when pressed OK Button
        self.data={}

        trial = self.sequence[self.number]

        if trial == 1:
            Window.unbind(mouse_pos=self.sound_on_сircle)
            Window.unbind(mouse_pos=self.sound_off_сircle)
            Window.unbind(mouse_pos=self.vis_circle_off)
            Window.unbind(mouse_pos=self.vis_circle_on)
            Window.bind(mouse_pos=self.sound_off)
            Window.bind(mouse_pos=self.sound_off)
            Window.bind(mouse_pos=self.vis_on)
            Window.bind(mouse_pos=self.vis_off)

        if trial == 0:
            Window.unbind(mouse_pos=self.sound_off)
            Window.unbind(mouse_pos=self.sound_off)
            Window.unbind(mouse_pos=self.vis_off)
            Window.unbind(mouse_pos=self.vis_on)
            Window.bind(mouse_pos=self.sound_on_сircle)
            Window.bind(mouse_pos=self.sound_off_сircle)
            Window.bind(mouse_pos=self.vis_circle_off)
            Window.bind(mouse_pos=self.vis_circle_on)

    def vis_on(self, w, p):
        if p[0] < 900 and p[0] > 700 and p[1] < 700 and p[1] > 500:
                #self.next_button.background_color = (0.5, 0.5, 0.5, 0.5)
                self.but.background_color = (1, 0, 0, 0.8)

    def vis_off(self, w, p):
        if not (p[0] < 900 and p[0] > 700 and p[1] < 700 and p[1] > 500):
                #self.next_button.background_color = (0.5, 0.5, 0.5, 0.5)
                self.but.background_color = (0, 0, 0, 1)

    def sound_on(self, w, p):
        if p[0] < 900 and p[0] > 700 and p[1] < 700 and p[1] > 500 and self.sound.state == 'stop':
            if self.sound:
                self.sound.play()

    def sound_off(self, w, p):
        if not (p[0] < 900 and p[0] > 700 and p[1] < 700 and p[1] > 500) and self.sound.state == 'play':
            if self.sound:
                print(self.sound)
                self.sound.stop()

    def vis_circle_on(self, w, p):
        if (((p[0] - 800) ** 2 + (p[1] - 600) ** 2) < 200 ** 2):
                #self.next_button.background_color = (0.5, 0.5, 0.5, 0.5)
                self.but.background_color = (1, 0, 0, 0.8)

    def vis_circle_off(self, w, p):
        if not (((p[0] - 800) ** 2 + (p[1] - 600) ** 2) < 200 ** 2):
                #self.next_button.background_color = (0.5, 0.5, 0.5, 0.5)
                self.but.background_color = (0, 0, 0, 1)


    def sound_on_сircle(self, w, p):
        if (((p[0] - 800) ** 2 + (p[1] - 600) ** 2) < 200 ** 2) and self.sound.state == 'stop':
            if self.sound:
                self.sound.play()

    def sound_off_сircle(self, w, p):
        if (((p[0] - 800) ** 2 + (p[1] - 600) ** 2) > 200 ** 2) and self.sound.state == 'play':
            if self.sound:
                print(self.sound)
                self.sound.stop()

    # def vis_off(self, w, p):
    #    if p[0] < 900 and p[0] > 700 and p[1] < 700 and p[1] > 500 and self.sound.state=='stop':
    #        if self.sound:
    #            self.sound.play()

    def next(self):

        if self.saved in (0, 1):
            self.saved = None
            self.number = self.number + 1

            if self.number < len(self.sequence):
                trial = self.sequence[self.number]

                if trial == 1:
                    Window.unbind(mouse_pos=self.sound_on_сircle)
                    Window.unbind(mouse_pos=self.sound_off_сircle)
                    Window.unbind(mouse_pos=self.vis_circle_off)
                    Window.unbind(mouse_pos=self.vis_circle_on)
                    Window.bind(mouse_pos=self.sound_off)
                    Window.bind(mouse_pos=self.sound_off)
                    Window.bind(mouse_pos=self.vis_on)
                    Window.bind(mouse_pos=self.vis_off)

                if trial == 0:
                    Window.unbind(mouse_pos=self.sound_off)
                    Window.unbind(mouse_pos=self.sound_off)
                    Window.unbind(mouse_pos=self.vis_off)
                    Window.unbind(mouse_pos=self.vis_on)
                    Window.bind(mouse_pos=self.sound_on_сircle)
                    Window.bind(mouse_pos=self.sound_off_сircle)
                    Window.bind(mouse_pos=self.vis_circle_off)
                    Window.bind(mouse_pos=self.vis_circle_on)

            else:
                App.get_running_app().stop()

        else:
            popup = Popup(title='Test popup',
                          content=Label(text='Выберите ответ'),
                          size_hint=(None, None), size=(400, 400))

            popup.open()

    def circle(self):
        self.current_answer = 0

    def square(self):
        self.current_answer = 1

    def ok(self):
        if self.current_answer in (0, 1):
            self.answers.append(self.current_answer)
            self.current_answer = None
            self.saved=1
            self.data['answers']=self.answers


            with open('data.json', 'w') as fp:
                json.dump(self.data, fp)
        else:
            print('exception')
            popup = Popup(title='Test popup',
                          content=Label(text='Выберитее ответ'),
                          size_hint=(None, None), size=(400, 400))

            popup.open()

class GridLayoutExample(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    #def __init__(self, **kwargs):
    #    super(CustomImage, self).__init__(**kwargs)


class TheLabApp(App):

    # сделать кнопку следюущий неактивной, пока не нажмут ок
    #
    def __init__(self):
        super().__init__()
        print(Window.size)
        self.gridLayoutExample=PageLayoutExample()




#class GridLayoutExample(GridLayOut)
#class BoxLayoutExample(BoxLayout):

TheLabApp().run()
