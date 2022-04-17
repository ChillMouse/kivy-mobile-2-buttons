from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

import numpy as np

class myApp(App):
    def build(self):

        s=Scatter(  do_rotation=False,
                    do_scale=False,
                    do_translation=False
                )

        fl=FloatLayout(
            size=(200, 500)
            )

        s.add_widget(fl)

        btn1 = Button(
            text="Это кнопка",
            font_size=20,
            on_press=self.btn_press,
            background_color=[0.4,0.2,0,1],
            background_normal='',
            size_hint=(.75, .1),
            pos=(100, 300)
            )

        btn2 = Button(
            text="Это почти кнопка",
            font_size=20,
            background_color=[0.4,0.2,0,1],
            background_normal='',
            size_hint=(.85, .1),
            pos=(100, 100)
            )

        fl.add_widget(btn1)
        fl.add_widget(btn2)
   
        return s
    def btn_press(self, instance):        
        instance.text='Я нажата'
        
if __name__=="__main__":
    myApp().run()