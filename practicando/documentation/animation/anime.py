from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

class Frame_1(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class MyApp(App):
    def build(self):
        layout = FloatLayout()
        self.btn = Button(text="Moverme", size_hint=(None, None), size=(100, 50), pos=(100, 100))
        self.btn.bind(on_press=self.animate_button)
        layout.add_widget(self.btn)
        return layout

    def animate_button(self, instance):
        # Mover el botón a la derecha y hacia arriba con aumento de tamaño
        anim = Animation(pos=(300, 400), size=(150, 70), duration=1.5, t='out_bounce')
        anim.start(self.btn)

MyApp().run()
