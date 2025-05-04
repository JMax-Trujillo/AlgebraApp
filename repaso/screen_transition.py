from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ScreenTransition(Button):
    def __init__(self, screen, direction="up", goal="home", **kw):
        super().__init__(**kw)
        self.screen = screen
        self.direction = direction
        self.goal = goal
        
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal    

class Welcome(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        master = BoxLayout(orientation='vertical', padding=20, spacing=20)
        master.add_widget(Label(
            text='Welcome to the Calculator',
            font_size='40sp'
        ))
        master.add_widget(ScreenTransition(
            self,direction='down', 
            goal='home',
            text='start',
            size_hint=(0.5,0.1),
            pos_hint={'center_x': 0.5}
        ))
        self.add_widget(master)

class Home(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.title = Label(text="Prueba de Transicion", font_size=40)
        self.sub_title = Label(text="Aqui tienes un contador", font_size=30)
        self.count_btn = Button(text='+ 1', font_size=20, size_hint_y=None, height=50)
        self.result = Label(text="0", font_size=30)
        
        self.count_btn.bind(on_press=self.plus_one)
        
        self.count_box = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.count_box.add_widget(self.title)
        self.count_box.add_widget(self.sub_title)
        self.count_box.add_widget(self.count_btn)
        self.count_box.add_widget(self.result)
        
        self.add_widget(self.count_box)
        

    def plus_one(self, instance):
        self.result.text = str(int(self.result.text) + 1)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Welcome(name='welcome'))
        sm.add_widget(Home(name='home'))
        
        return sm
if __name__ == '__main__':
    MainApp().run()