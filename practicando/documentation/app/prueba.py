from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.borderless = True  # Quitar barra del sistema
Window.size = (600, 400)

class Barra(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 30

        self.add_widget(Button(text="Min", on_release=self.minimizar))
        self.add_widget(Button(text="Cerrar", on_release=self.cerrar))

    def minimizar(self, *args):
        Window.minimize()

    def cerrar(self, *args):
        App.get_running_app().stop()

class MiApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        root.add_widget(Barra())  # Tu "barra de título" personalizada
        return root

if __name__ == '__main__':
    MiApp().run()
