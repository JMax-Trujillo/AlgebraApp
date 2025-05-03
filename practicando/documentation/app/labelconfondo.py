from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle

class Labelconfondo(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        with self.canvas.before:
            Color(0,1,0,1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            
        self.bind(pos=self.actualizar, size=self.actualizar)
    
    def actualizar(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class MyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Labelconfondo(
            size_hint=(None, None),
            text="Maxito",
            color=(1,0,0,1),
            width=150,
            height=200,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        ))

class practicaFondoApp(App):
    def build(self):
        return MyFloatLayout()

if __name__ == '__main__':
    practicaFondoApp().run()