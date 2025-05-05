# All Kivy Imports 
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

# Other Needed Imports

# Screen transition
class LoginScreen(Button):
    # añadir parametros para modificar las caracteristicas de el screen
    def __init__(self, screen, direction='up', goal='home' ,**kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
        self.size_hint_y = None
        self.height = 100
        print("LoginScreen")

        
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal
    
# Login
class Login(BoxLayout):
    def __init__(self, screen,**kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.orientation = 'vertical'
        self.size_hint = (.4,.5)
        self.pos_hint = {'center_x':.5}
        self.spacing = 10
        self.padding = 10
        print("Login")

        login = Label(text='Login', font_size=40)
        username = TextInput(hint_text='Username', font_size=20, size_hint_y=None, height=100)
        password = TextInput(hint_text='Password', font_size=20, password=True, size_hint_y=None, height=100)
        btn_screen = LoginScreen(
            screen,
            direction='up', 
            goal='home',
            text='start',
            font_size=20
            )
        self.add_widget(login)
        self.add_widget(username)
        self.add_widget(password)
        self.add_widget(btn_screen)


# Initial Welcome Screen
class Welcome(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        master = FloatLayout()
        backgroud = Image(
            source='../assets/img/login_fondo.png',
            allow_stretch=True,
            keep_ratio=False
            )
        centro = Login(self)
        master.add_widget(backgroud)
        master.add_widget(centro)
        self.add_widget(master)
        print("Welcome")

# Home Screen
class Home(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.initUI()
        print("Home")
    
    def initUI(self):
        # Todas los widgets y layouts
        # Separar variables para layouts, y ordenadamento añadir los widgets que se van creando
        titulo = Label(text='Holaaaaa', font_size=40)
        self.add_widget(titulo)
    
# Our  Main App
class MainApp(App):
    #App Builder
    def build(self):
        sm = ScreenManager()
        print('screenmanager')
        sm.add_widget(Welcome(name='welcome'))
        print('welcome')
        sm.add_widget(Home(name='home'))
        print('home')
        return sm

if __name__ == '__main__':
    MainApp().run()