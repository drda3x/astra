#!/ust/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ListProperty

def get_color(*rgb):
    return map(lambda x: x/255.0, rgb)


class LoginLayout(BoxLayout):
    pass

class AstraApp(App):

    def build(self):
        Window.clearcolor = get_color(254, 247, 219) + [1]
        return LoginLayout()


if __name__ == '__main__':
    AstraApp().run()