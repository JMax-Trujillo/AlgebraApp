from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Pantalla1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        btn = Button(text="Ir a pantalla 2")
        btn.bind(on_press=self.cambiar)
        layout.add_widget(btn)
        self.add_widget(layout)

    def cambiar(self, instance):
        self.manager.current = 'pantalla2'

class Pantalla2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        btn = Button(text="Volver a pantalla 1")
        btn.bind(on_press=self.cambiar)
        layout.add_widget(btn)
        self.add_widget(layout)

    def cambiar(self, instance):
        self.manager.current = 'pantalla1'

class DemoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Pantalla1(name='pantalla1'))
        sm.add_widget(Pantalla2(name='pantalla2'))
        return sm

if __name__ == '__main__':
    DemoApp().run()
