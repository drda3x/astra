#!/ust/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App as KivyAppClass
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen, ScreenManager as ScreenManagerOrigin


class LoginScreen(Screen):
    pass


class ChoiceScreen(Screen):
    pass


class ScreenManager(ScreenManagerOrigin):
    pass


root_widget = Builder.load_string('''
FloatLayout:
    Image:
        source: 'fon.png'
        allow_stretch: True
        keep_ratio: False
    BoxLayout:
        id: container
        orientation: 'vertical'
        size_hint: 0.5, 0.3
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        Label:
            text: 'Введите код с экрана компьютера'
            color: [0,0,0,1]
        TextInput:
            height: 100
            text: '18-116'
            # Нужно будет найти соотношение размера шрифта при изменении
            # размеров окна
            padding_x: [(container.width / 2) - len(self.text) * 14, 0]
            font_size: 50
            id: inp
        Button:
            text: 'Подключиться'
''')


class App(KivyAppClass):

    def build(self):
        return root_widget


if __name__ == '__main__':
    App().run()

