from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ContenidoEnCelda(BoxLayout):
    def __init__(self, texto_base, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        for i in range(3):
            self.add_widget(Button(text=f"{texto_base} - {i+1}"))

class MiInterfaz(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2  # 2 columnas
        # self.rows = 2  # 2 filas
        self.spacing = 10
        self.padding = 10

        for i in range(4):
            box = ContenidoEnCelda(f"Box {i+1}")
            self.add_widget(box)
            

class AppDemo(App):
    def build(self):
        return MiInterfaz()

if __name__ == '__main__':
    AppDemo().run()
