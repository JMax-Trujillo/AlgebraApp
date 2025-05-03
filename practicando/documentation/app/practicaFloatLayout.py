from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Flotantes(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.add_widget(Button(
            text="Maxito",
            size_hint=(.2, .1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_normal="",
            background_color=(0,1,0,1)
        ))
        
        self.add_widget(Label(
            text="Maxito",
            size_hint=(None, None),
            width=250,
            height=200,
            pos_hint={'center_x': 0.1, 'center_y': 0.2}
        ))

class PracticaFloatLayoutApp(App):
    def build(self):
        return Flotantes()

if __name__ == '__main__':
    PracticaFloatLayoutApp().run()