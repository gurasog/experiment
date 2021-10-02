from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ListProperty, BooleanProperty, DictProperty
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class SoundPlayer(BoxLayout):

    def play_sound(self):
        sound=SoundLoader.load('sound.mp3')
        if sound:
            sound.play()

class CustomImage(Image):

    colors=ListProperty()
    oldSegment_buffer = ListProperty()
    segment_color = ListProperty()
    moveSegment_color = ListProperty()
    id2 = StringProperty('')

    def __init__(self, **kwargs):
        super(CustomImage, self).__init__(**kwargs)
        self.colors = [[0.5, 0.00, 0.8], [0.16, 0.78, 0.88], [0.31, 0.63, 0.06], [0.95, 0.37, 0.39], [0.35, 0.35, 0.82],
                       [0.99, 0.90, 0.05], [0.93, 0.54, 0.14], [0.93, 0.24, 0.89], [0.64, 0.38, 0.00],
                       [0.12, 0.74, 0.48], [0.93, 0.18, 0.55], [0.98, 0.45, 0.37], [0.09, 0.22, 0.25]]

    def paintbrush(self):
        with self.canvas:
            for lineObj in self.segment_color:
                lineObj.a = 0.5
            #self.get_parent_window().children[-1].sensationNumber += int(1)

    def on_touch_down(self, touch):

        stencilobj = self.get_root_window().children[-1].ids['floatStencilArea']

        if self.collide_point(touch.x, touch.y):
            stencilobj.currImage = self.id2
            stencilobj.currImagename = self.imglabel
            stencilobj.buttonPress = False
            with self.canvas:
                self.segment_color.append(
                    Color(*self.colors[int(self.get_parent_window().children[-1].sensationNumber % 13)]))
                touch.ud['line'] = Line(width=5, points=(touch.x, touch.y))
            return True


    def on_touch_move(self, touch):
        stencilobj = self.get_root_window().children[-1].ids['floatStencilArea']

        if not stencilobj.buttonPress:
            if self.collide_point(touch.x, touch.y) and 'line' in touch.ud.keys():
                touch.ud['line'].points += [touch.x, touch.y]
                return True


    def on_touch_up(self, touch):

        stencilobj = self.get_root_window().children[-1].ids['floatStencilArea']

        if not stencilobj.buttonPress:
            if self.collide_point(touch.x, touch.y):
                if 'line' in touch.ud.keys():

                    currentimg = stencilobj.currImagename
                    sensekey = 'sensation'+str(self.get_parent_window().children[-1].sensationNumber)+'_'+currentimg

                    if sensekey in stencilobj.lineDict.keys():
                        stencilobj.lineDict[sensekey] += touch.ud['line'].points
                    else:
                        stencilobj.lineDict[sensekey] = touch.ud['line'].points

                    self.save_png(0)

                    # PLACEHOLDER: send message with pixel coordinates
                    return True

                else:
                    return True

        else:
            stencilobj.buttonPress = False
            return True


class TheLabApp(App):

    def __init__(self):
        super().__init__()
        self.sound = SoundLoader.load('sound.mp3')
        self.sequence=[1,0,0,1,1]
        self.number=0
        self.answers=[]
        self.current_answer=None

        Window.bind(mouse_pos=self.sound_on)
        Window.bind(mouse_pos=self.sound_off)

    def sound_on(self, w, p):
        if p[0] < 100 and p[1] < 100 and self.sound.state=='stop':
            if self.sound:
                self.sound.play()

    def sound_off(self,w,p):
        if (p[0] > 100 or p[1] > 100) and self.sound.state=='play' :
            if self.sound:
                print(self.sound)
                self.sound.stop()


    def sound_on_сircle(self, w, p):
        if (((p[0] - 200) ** 2 + (p[1] - 200) ** 2) < 200 ** 2) and self.sound.state == 'stop':
            if self.sound:
                self.sound.play()

    def sound_off_сircle(self,w,p):
        if (((p[0] - 200) ** 2 + (p[1] - 200) ** 2) > 200**2) and self.sound.state == 'play':
            if self.sound:
                print(self.sound)
                self.sound.stop()

    def next(self):

        if self.current_answer in (0, 1):

        self.number=self.number+1

        if self.number< len(self.sequence):
            trial=self.sequence[self.number]

            if trial==1:
                Window.unbind(mouse_pos=self.sound_on_сircle)
                Window.unbind(mouse_pos=self.sound_off_сircle)
                Window.bind(mouse_pos=self.sound_off)
                Window.bind(mouse_pos=self.sound_off)


            if trial==0:
                Window.unbind(mouse_pos=self.sound_off)
                Window.unbind(mouse_pos=self.sound_off)
                Window.bind(mouse_pos=self.sound_on_сircle)
                Window.bind(mouse_pos=self.sound_off_сircle)
        else:
            App.get_running_app().stop()

    def circle(self):
        self.current_answer=0

    def square(self):
        self.current_answer = 1

    def ok(self):
        if self.current_answer in (0,1):
            self.answers.append(self.current_answer)
            self.current_answer=None
        else:
            print('exception')
            popup = Popup(title='Test popup',
                          content=Label(text='Выберитее ответ'),
                          size_hint=(None, None), size=(400, 400))

            popup.open()

#class GridLayoutExample(GridLayOut)
#class BoxLayoutExample(BoxLayout):

TheLabApp().run()
