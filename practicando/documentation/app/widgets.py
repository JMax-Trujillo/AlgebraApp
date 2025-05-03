from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cols=1
        
        self.add_widget(Label(
            text="Makanaki la realeza",
            font_size=32,
            color=(1,0.56,0,1)
        ))
        
        self.add_widget(CheckBox(
            active=False,
            size_hint=(1, 1)
        ))
        
        self.add_widget(Button(
            text="Makanaki la realeza",
            background_color=(0.14,0.54,1.00,1),
            color=(1,1,1,1)
        ))
        
        self.add_widget(TextInput(
            multiline=False,
            text="Makanaki la realeza",
            background_color=(0.14,0.54,1.00,1),
            foreground_color=(1,1,1,1)
        ))
        
        self.add_widget(Slider(
            min=0,
            max=100,
            value=50,
            step=1,
            orientation='horizontal',
            value_track_color=(1,0,1,1)
        ))
        
        self.add_widget(Image(
            source=("../../../assets/Palette.png"),
            size_hint_y=None,
            height=300,
            allow_stretch= True
            ))
        
        self.add_widget(Switch(
            size_hint=(1, 1)
        ))

class MyFirstApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyFirstApp().run()