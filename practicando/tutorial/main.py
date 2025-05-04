# All Kivy Imports 

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen, ScreenManager

# Other Needed Imports

from languages import *
# from googletrans import Translator
import speech_recognition as sr



# Screen transition

# Initial Welcome Screen

# Home Screen

class Home(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initUI()

    # Out Design
    def initUI(self):
        # Create App Widgets
        self.title = Label(text="PyLator", font_size="55sp", font_name="DejaVuSans")
        self.input_option = DropDown()
        self.output_option = DropDown()
        self.btn_reverse = Button(text="Reverse", on_press=self.reverse_text, size_hint=(1,0.2), pos_hint={'center_x':0.5})
        self.btn_clear = Button(text="Reset", on_press=self.clear_boxes,size_hint=(0.8,0.4), pos_hint={'center_x':0.5})
        self.btn_translate = Button(text="Translate", size_hint=(0.8,0.4), pos_hint={'center_x':0.5}) # , on_press=self.translate_text
        self.btn_speak = Button(text="Speak", on_press=self.speak_to_translate,size_hint=(0.8,0.4), pos_hint={'center_x':0.5})
        self.btn_reset = Button(text="Reset", size_hint=(0.8,0.4), pos_hint={'center_x':0.5})
        
        self.input_box = TextInput(hint_text='Enter text to translate', size_hint=(1, 0.8))
        self.output_box = TextInput(hint_text='Translation will appear here', size_hint=(1, 0.8), readonly=True)
        
        # Create Dropdown List
        
        for lang in values:
            input_btn = Button(text=lang, size_hint_y=None, height=44)
            input_btn.bind(on_release=lambda btn: self.update_btn_text(self.input_button, btn.text))
            self.input_option.add_widget(input_btn)
            
            output_btn = Button(text=lang, size_hint_y=None, height=44)
            output_btn.bind(on_release=lambda btn: self.update_btn_text(self.output_button, btn.text))
            self.output_option.add_widget(output_btn)
        
        self.input_button = Button(text="Select Input Language", size_hint=(0.7,0.4), pos_hint={'center_x':0.5})
        self.output_button = Button(text="Select Output Language", size_hint=(0.7,0.4), pos_hint={'center_x':0.5})
        
        self.input_button.bind(on_release=self.input_option.open)
        self.output_button.bind(on_release=self.output_option.open)
        
        # Add Widgets to our Design (App Layout)
        
        self.master = BoxLayout()
        col1 = BoxLayout(orientation='vertical', padding=15)
        col2 = BoxLayout(orientation='vertical', padding=15)
        
        col1.add_widget(self.title)
        col1.add_widget(self.input_button)
        col1.add_widget(self.output_button)
        col1.add_widget(self.btn_translate)
        col1.add_widget(self.btn_speak)
        col1.add_widget(self.btn_reset)
        
        col2.add_widget(self.input_box)
        col2.add_widget(self.btn_reverse)
        col2.add_widget(self.output_box)
        
        self.master.add_widget(col1)
        self.master.add_widget(col2)
        
        self.add_widget(self.master)

    def update_btn_text(self, button, text):
        button.text=text

    # # Translate text
    # def translate_text(self, instance=None):
    #     source_lang = self.input_button.text
    #     dest_lang = self.input_button.text
    #     text = self.input_box.text
        
    #     try:
    #         translate_text = Translator()
    #         res = translate_text.translate(text, src=source_lang, dest=dest_lang).text
    #         self.output_box.text = res
    #     except Exception as e:
    #         print(f'Error: {e}')
    #         self.output_box.text="Error...."
    
    # # Recognize spoken speech
    # def recogonize_speech(self, instance=None):
    #     listener = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         try:
    #             audio = listener(source, timeout=5)
    #             text = listener.recognize_google(audio)
    #             return text
    #         except sr.UnknownValueError:
    #             print("Could not understand audio")
    #         except sr.RequestError as e:
    #             print(f'Error requesting speech recognition results {e}')
    #         except Exception as e:
    #             print(f'Error recognizing speech: {e}')

    # Speak text is translated
    def speak_to_translate(self, instance=None):
        txt = self.recogonize_speech()
        if txt:
            self.input_box.text = txt
            self.speak_to_translate()

    # Clear all boxes when reset
    def clear_boxes(self, instance=None):
        self.input_box.text = ""
        self.output_box.text = ""

    # Reverse the text and languages
    def reverse_text(self, instance=None):
        input_text = self.input_box.text
        output_text = self.output_box.text
        
        self.input_box.text = output_text
        self.output_box.text = input_text
        
        input_lang = self.input_button.text
        output_lang = self.output_button.text
        
        self.input_button.text = input_lang
        self.output_button.text = output_lang

# Our  Main App
class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name="home"))

        return sm
#App Builder

if __name__ == '__main__':
    MainApp().run()