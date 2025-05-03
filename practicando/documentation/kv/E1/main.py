from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('my.kv')

class MiInterfaz(BoxLayout):
    def saludar(self):
        nombre = self.ids.caja_texto.text
        if nombre.strip():
            self.ids.etiqueta.text = f"Hola, {nombre} 👋"
        else:
            self.ids.etiqueta.text = "Escribe tu nombre, por favor."

class MiApp(App):
    def build(self):
        return MiInterfaz()

MiApp().run()
