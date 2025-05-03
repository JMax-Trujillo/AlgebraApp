from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle


# Builder.load_file('my.kv')

class Principal(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10, 20, 10, 20]
        self.spacing = 5
        self.size_hint = (None, None)
        self.size = (320, 250)
        self.pos_hint={"center_x": 0.5, "center_y": 0.5}

        with self.canvas.before:
            Color(1,1,1,0.2)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        self.add_widget(Label(
            text="Login", 
            font_size=24, 
            size_hint_y=None, 
            height=40
            ))
        self.add_widget(TextInput(
            hint_text="Username", 
            size_hint_y=None, 
            height=30
            ))
        self.add_widget(TextInput(
            hint_text="Password", 
            password=True, 
            size_hint_y=None, 
            height=30
            ))
        self.add_widget(Button(
            text="Login", 
            size_hint_y=None, 
            height=35
            ))

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class Card(GridLayout):
    pass

class MyApp(App):
    def build(self):
        return Principal()

if __name__ == '__main__':
    MyApp().run()