from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MenuPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Button(text="Ir a Ajustes", on_release=lambda x: self.change_screen('ajustes')))
        layout.add_widget(Button(text="Ir a Resultados", on_release=lambda x: self.change_screen('resultados')))
        layout.add_widget(Button(text="Ir a Ayuda", on_release=lambda x: self.change_screen('ayuda')))
        self.add_widget(layout)

    def change_screen(self, screen_name):
        self.manager.current = screen_name


class Ajustes(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Button(text="Ajuste 1"))
        layout.add_widget(Button(text="Volver al Menú", on_release=lambda x: self.change_screen('menu')))
        self.add_widget(layout)
    
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class Resultados(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Button(text="Mostrar Resultados"))
        layout.add_widget(Button(text="Volver al Menú", on_release=lambda x: self.change_screen('menu')))
        self.add_widget(layout)

    def change_screen(self, screen_name):
        self.manager.current = screen_name

class Ayuda(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Button(text="Información de Ayuda"))
        layout.add_widget(Button(text="Volver al Menú", on_release=lambda x: self.change_screen('menu')))
        self.add_widget(layout)

    def change_screen(self, screen_name):
        self.manager.current = screen_name

class MiApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuPrincipal(name='menu'))
        sm.add_widget(Ajustes(name='ajustes'))
        sm.add_widget(Resultados(name='resultados'))
        sm.add_widget(Ayuda(name='ayuda'))
        return sm


if __name__ == '__main__':
    MiApp().run()
