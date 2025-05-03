from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.add_widget(Label(
            text="Interfaz Futurista",
            font_size=32,
            color=(1, 0.56, 0, 1)  # naranja_vivo
        ))

        self.add_widget(Button(
            text="Botón Primario",
            background_color=(0.14, 0.54, 1.00, 1),  # azul_electrico
            color=(1, 1, 1, 1)
        ))

        self.add_widget(Button(
            text="Botón Secundario",
            background_color=(0.42, 0.37, 0.71, 1),  # violeta_tenue
            color=(1, 1, 1, 1)
        ))

class MyApp(App):
    def build(self):
        Window.clearcolor = (0.04, 0.11, 0.21, 1)  # azul_oscuro
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()
