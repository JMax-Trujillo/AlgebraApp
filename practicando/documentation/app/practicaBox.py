from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Caja(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        
        self.add_widget(Label(
            text="Maxito",
            font_size=25,
            color=(0,1,1,1)
        ))
        
        self.textinput = TextInput(
            font_size=25,
        )
        
        self.add_widget(self.textinput)
        
        self.add_widget(Button(
            text="Press",
            background_color=(1,0,1,1),
            on_press=self.press
        ))
    def press(self, instance):
        print(f'Mi nombre es {self.textinput.text}')
        self.textinput.text = ''


class PosicionApp(App):
    def build(self):
        return Caja()

if __name__ == '__main__':
    PosicionApp().run()














































# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout

# class MyApp(App):
#     def build(self):
#         layout = BoxLayout(orientation='horizontal')
#         layout.add_widget(Button(text="Botón 1"))
#         layout.add_widget(Button(text="Botón 2"))
#         return layout

# MyApp().run()

# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button

# class MyApp(App):
#     def build(self):
#         layout = GridLayout(cols=4)
#         for i in range(16):
#             layout.add_widget(Button(text=f"Botón {i+1}"))
#         return layout

# MyApp().run()

# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.floatlayout import FloatLayout

# class MyApp(App):
#     def build(self):
#         layout = FloatLayout()
#         btn = Button(text="Flotando", size_hint=(.3, .2), pos_hint={'center_x': .5, 'center_y': .5})
#         layout.add_widget(btn)
#         return layout

# MyApp().run()
