from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class rejillaxd(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 10
        self.spacing = 5
        self.cols = 2
        
        for i in range(10):
            self.add_widget(Button(
                text="Maxito",
                font_size=32,
                color=(0,1,1,1),
                on_press=self.press
            ))
    def press(self, instance):
        self.add_widget(Label(
            text="Maxito",
            font_size=30,
            color=(1,1,1,1)
        ))

class practicaGridApp(App):
    def build(self):
        return rejillaxd()

if __name__ == '__main__':
    practicaGridApp().run()