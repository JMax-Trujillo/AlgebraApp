from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SaludoApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.entrada = TextInput(hint_text="Escribe tu nombre", multiline=False)
        self.boton = Button(text="Saludar", on_press=self.saludar)
        self.etiqueta = Label(text="Esperando saludo...")

        self.layout.add_widget(self.entrada)
        self.layout.add_widget(self.boton)
        self.layout.add_widget(self.etiqueta)

        return self.layout

    def saludar(self, instance):
        nombre = self.entrada.text.strip()
        if nombre:
            self.etiqueta.text = f"Hola, {nombre} 👋"
        else:
            self.etiqueta.text = "Por favor, escribe tu nombre."

SaludoApp().run()
